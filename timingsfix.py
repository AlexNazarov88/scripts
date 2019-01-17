"""
Author: Oleksandr Nazarov - aleksandr.nazarov@vokigames.com
Voki Games

Script to fix timing text files with a hard coded preset
	
Needs to be placed in: C:/Users/*YOUR USER*/Documents/maya/2016/scripts
How to use in Maya:
	import timingsfix
	timingsfix.fixTiming()

to do: need to add junk text strip
"""

import re
import argparse
import maya.OpenMaya as OpenMaya
import maya.cmds as cmds
import os
#import glob

filePreset = "timing.txt"

def stripString(source):
	strippedSpaces = re.sub(r'[\t+\v+]', "", source)
	strippedChars = re.sub('-', " ", strippedSpaces)

	return strippedChars

def readFile():
	global filePreset

	# to do: add check for other txt files containing timings
	 
	# elif not filePath == filePreset:
	# 	print 'Default file name not found, looking for other files...'
	# 	timingsFile = glob.glob('*.txt')
	# 	if timingsFile =='':
	# 		raise RuntimeError, 'No .txt files found.'
	# 	elif not timingsFile.endswith('.txt'):
	# 		raise RuntimeError, 'Wrong extension, txt file expexted.'
	
	sceneDir = os.path.dirname(cmds.file(location = True , query = True )) + "/"
	timingsFile = sceneDir + filePreset
	print timingsFile

	fileContents = ""
	file = open(timingsFile, "r")
	if file.mode == 'r':
		fileContents = file.read()
		file.close()
	
	return fileContents

def writeFile(contentsToWrite, filePath = filePreset):
	file = open(filePath, "w")
	if file.mode == 'w':
		file.write(contentsToWrite)
		file.close()

def fixTiming():
	# function for maya integration
	fileContents = ""

	OpenMaya.MGlobal.displayInfo('Fixing timings file...')

	fileContents = readFile()
	stringToWrite = stripString(fileContents)
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