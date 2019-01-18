"""

Author: Oleksandr Nazarov - aleksandr.nazarov@vokigames.com
Voki Games

This script needs to be added to:
C:/Users/*Your User*/Documents/maya/2016/scripts

 .ma to .fbx exporter - save current maya ascii scene to .fbx file 

usage:
	import matofbx
	matofbx.start()

"""
import sys
sys.dont_write_bytecode = True

import os
import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import re


def load(fileName):
	OpenMaya.MGlobal.displayInfo('Loading exported scene: ' + fileName)
	cmds.file( fileName, open=True, force=True  ) 
	

def getName():
	sceneName = cmds.file(sceneName = True, shortName = True , query = True )
	OpenMaya.MGlobal.displayInfo('Current scene name: ' + sceneName)
	return sceneName


def getDir():
	sceneDir = os.path.dirname(cmds.file(location = True , query = True ))
	return sceneDir + "/"
	

def start():
	OpenMaya.MGlobal.displayInfo('Starting .ma to .fbx export...')
	
	sceneName = getName()
	sceneDir = getDir()
	finalName = ''

	if sceneName.endswith( '.ma' ):
		sceneName = re.sub('\.ma$', '', sceneName)
		sceneName += '.fbx' 
		finalName = sceneDir +  sceneName

		cmds.file( rename= finalName)
		cmds.file( exportAll=True)
		OpenMaya.MGlobal.displayInfo('Scene has been exported to fbx.')

	load(finalName)
	OpenMaya.MGlobal.displayInfo('Export successful!')

	
