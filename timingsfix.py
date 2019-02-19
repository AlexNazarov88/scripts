#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Oleksandr Nazarov - aleksandr.nazarov@vokigames.com
# Voki Games
# 
# Script to fix timing text files with a hard coded preset
# v0.3
# 
# Needs to be placed in: C:/Users/*YOUR USER*/Documents/maya/2016/scripts
# How to use in Maya:
# 	import timingsfix
# 	timingsfix.fixTiming()

# to do: add exceptions

import sys
sys.dont_write_bytecode = True

import re
import argparse
import maya.OpenMaya as OpenMaya
import maya.cmds as cmds
import os
#import glob

FILEPRESET = "timing.txt"
regex = r"(in_out)|(cycle)|(IN - OUT)|(IN-OUT)|(\bIN\b)|(\bout\b)|(revers)|(start)|(pose)|([-])"


def getProjDir():
	projDir = os.path.dirname(cmds.file(location = True , query = True )) + "/"
	return projDir


def stripString(source):
	global regex
	OpenMaya.MGlobal.displayInfo('Clearing timings... ')
	strippedSpaces = re.sub(r'[\t+\v+]', " ", source)
	# strippedChars = re.sub(r'[-]', " ", strippedSpaces)
	strippedEtc = re.sub(regex, " ", strippedSpaces, flags=re.IGNORECASE) 
	return strippedEtc


def makePreset(source):
	# to do, add preset parser/writer
	# matches exactly one (first) time to correct starting frame
	fixedStartFrames = re.sub(r'1', '0', source, count=1) 
	return fixedStartFrames


def readFile():
	global FILEPRESET
	timingsFile = getProjDir() + FILEPRESET
	fileContents = ""
	file = open(timingsFile, "r")
	if file.mode == 'r':
		fileContents = file.read()
		OpenMaya.MGlobal.displayInfo('Reading... ')
		OpenMaya.MGlobal.displayInfo(fileContents)
		file.close()
	return fileContents
	# to do: add check for other txt files containing timings
	# elif not filePath == filePreset:
	# 	print 'Default file name not found, looking for other files...'
	# 	timingsFile = glob.glob('*.txt')
	# 	if timingsFile =='':
	# 		raise RuntimeError, 'No .txt files found.'
	# 	elif not timingsFile.endswith('.txt'):
	# 		raise RuntimeError, 'Wrong extension, txt file expexted.'


def writeFile(contentsToWrite): 
	global FILEPRESET
	fileName = getProjDir() + FILEPRESET
	file = open(fileName, "w")
	if file.mode == 'w':
		OpenMaya.MGlobal.displayInfo('Writing... ')
		OpenMaya.MGlobal.displayInfo(contentsToWrite)
		file.write(contentsToWrite)
		file.close()


def fixTiming():
	# function for maya integration
	fileContents = ""
	OpenMaya.MGlobal.displayInfo('Fixing timings file...')
	fileContents = readFile()
	stringToWrite = stripString(fileContents)
	# matchedToPattern = makePreset(stringToWrite)
	writeFile(stringToWrite)
	OpenMaya.MGlobal.displayInfo('Done!')


# if __name__ == "__main__":
# 	fileContents = ""
# 	parser = argparse.ArgumentParser()

# 	parser.add_argument("filePath", help = "path to text file")
# 	args = parser.parse_args()
# 	print "Parsing file..."

# 	fileContents = readFile(args.filePath)
# 	stringToWrite = stripString(fileContents)
# 	writeFile(stringToWrite, args.filePath)
# 	print "Done!"