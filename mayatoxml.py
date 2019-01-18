"""
Author: Oleksandr Nazarov - aleksandr.nazarov@vokigames.com
Voki Games

This script needs to be added to:
C:/Users/*Your User*/Documents/maya/2016/scripts
usage:
    select needed bones/transformations/groups

    run selectively:
        import mayatoxml
        mayatoxml.factory()

    run all:
        import mayatoxml
        mayatoxml.factory(True)
"""


import sys
sys.dont_write_bytecode = True

import maya.cmds as cmds
#import maya.mel as mel
import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim
import cvxporter2 as xporter
import argparse
import os
from time import localtime, strftime
import timingsfix

defaultAnimFile = "timing.txt"

# def getProjName(): 
#     # gets the name of maya project file
#     projName = cmds.workspace(shortName = True) 
#     return projName.lower() # lower() may be needed as project name sometimes comes in capitals 

def getAnimsFile():
    fileName = os.getcwd() + "/" + defaultAnimFile # may not work in some situations
    return fileName


def createXML(): 
    fileName = 'export_' + strftime("%d-%m-%Y_%H%M", localtime())
    if not fileName.endswith( '.xml' ):
        fileName += '.xml'

    OpenMaya.MGlobal.displayInfo('FileName: ' + fileName)

    try:
        file = open(fileName)
    except IOError:
        # If not exists, create the file
        file = open(fileName, 'w+')

    file.close() 

    OpenMaya.MGlobal.displayInfo('create XML: ' + fileName)
    return fileName 


def setXMLFile(filePath): 
    xporter.onXMLFileAddressChanged(filePath)

def setAnimFile(filePath): 
    xporter.onAnimationsFileAddressChanged(filePath)
    # needed because it`s not getting triggered with onAnimationsFileAddressChanged()
    xporter.loadAnimationsFromFile() 

def runSelectiveExport(): 
    # need to add error handling - try except
    OpenMaya.MGlobal.displayInfo('Starting selective export...')
    xporter.doExport(False) 


def runAllExport(): # test
    # need to add error handling - try except
    OpenMaya.MGlobal.displayInfo('Starting export everything...')
    xporter.doExport(True) 


def factory(all = False):
    # main function
    xmlFile = ''
    animFile = ''
    
    xmlFile = createXML()
    setXMLFile(xmlFile)
    
    # to do: improve animation timings file check up
    timingsfix.fixTiming()
    animFile = getAnimsFile()
    setAnimFile(animFile)
    #

    # run exporting process
    if all:
        runAllExport()
    else:
        runSelectiveExport()


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     # to do: improve argument parser
#     parser.add_argument("preset", help = "personage preset", type = string)
#     parser.add_argument("fileName", help = "export file name", type = string)
#     # maybe add additional flags such as -i "export with item"  
#     args = parser.parse_args()
#     factory(args.preset, args.fileName)