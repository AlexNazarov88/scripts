"""
Author: Oleksandr Nazarov - aleksandr.nazarov@vokigames.com
Voki Games

maya xml model to bin converter wrapper for convenience

usage:
    in console, run: 
    python xml-to-bin.py *PATH TO FILE*

"""
import sys
sys.dont_write_bytecode = True

import os
sys.path.insert(1, os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'utils', 'resbuilder'))
import script
import fnmatch
import glob
import re
import argparse

from subprocess import check_call

# commented because ver3 is used by default now
# def repo():
# 	return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# # need to add check for old items
# oldDir = os.path.join(repo(), 'base_mm', 'models', 'Items')
# old = ['axe.xml', \
# 		'BookNormal.xml', 'brush_mm.xml', \
# 		'CoffeeCup.xml', \
# 		'golf_klugka.xml', 'grably.xml', 'guitar_mm.xml', \
# 		'Item_Bagor.xml', 'Item_BirdCage.xml', 'Item_CardBox.xml', \
# 		'kiy.xml', \
# 		'Lantern.xml', 'letter.xml', \
# 		'metla.xml', \
# 		'palka.xml', 'paper.xml', 'pen.xml', \
# 		'scissors.xml', 'shovel.xml', 'spray.xml', 'super_grably.xml', 'swing.xml', \
# 		'tabletpc.xml', 'trubka.xml', 'kost.xml', 'leyka.xml']

def bin_factory(folder):

    # to do: add method to process single file inputs

    toMerge = getMergeList(folder)
    if toMerge:
        merge_models(toMerge)
    
    toBin = getToBinList(folder, toMerge)
    if toBin:
        to_bin_models(toBin)

    # wait for escape
    script.pause()


def merge_models(modelsList = []):
    # merges object of similar type into one
    print "#  Merging models...  #"
    fileNames = []
    for file in modelsList:
        splitted = re.sub(r"[.](.*)[.]xml", '', file)
        fileNames.append(splitted)
    
    toMergeList = list(set(fileNames))
    merged = []
    try:
        for model in toMergeList:
            exists = os.path.isfile(model + '.xml.bin')
            if exists:
                merged.append(model)
            else:    
                debug = os.path.basename(model)
                print('MODEL NAME: ' + os.path.splitext(debug)[0])
                check_call(['python', '-B', os.path.join('binpy', 'merge_models_xml.py'), model])
    except Exception:
		print('Failed to merge: ' + os.path.basename(model))
		sys.exit(1)
    
    print '#  These models are already merged:  #'
    for model in merged:
        debug = os.path.basename(model)
        print(os.path.splitext(debug)[0])


def to_bin_models(modelsList = [], ver = 3):
	# converts xml model to binary
    # currently, the default compression model is set to 3 for all models
    print "#  Converting models to bin...  #"
    binned = []
    try:
        for model in modelsList:
            exists = os.path.isfile(model + '.bin')
            if exists:
                binned.append(model)
            else:
                debug = os.path.basename(model)
                print(os.path.splitext(debug)[0])
                check_call(['python', '-B', os.path.join('binpy', 'modelxmltobin.py'), '-' + str(ver), model])
                # script.run(['pack_file', model + '.bin'])
    except Exception:
        print('Failed ' + model)
        sys.exit(1)
    
    print '#  These models are already binned:  #'
    for model in binned:
        debug = os.path.basename(model)
        print(os.path.splitext(debug)[0])


def getMergeList(folder):
    foundFiles = glob.glob(folder + "/*.*.xml")
    return foundFiles


def getToBinList(folder, skip = []):
    foundFiles = glob.glob(folder + "/*.xml") 
    
    for file in skip:
        foundFiles.remove(file)

    ToBinList = []
    for file in foundFiles:
        ToBinList.append(file)  
    return ToBinList


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("dirPath", help = "directory path to parse and binarize xml files")
    args = parser.parse_args()
    bin_factory(args.dirPath)
