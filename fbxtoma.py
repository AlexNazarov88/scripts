"""

Author: Oleksandr Nazarov - aleksandr.nazarov@vokigames.com
Voki Games

This script needs to be added to:
C:/Users/*Your User*/Documents/maya/2016/scripts

.fbx to .ma exporter - save current fbx scene to maya ascii file 

usage:
	import fbxtoma
	fbxtoma.start()

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
	OpenMaya.MGlobal.displayInfo('Starting .fbx to .ma export...')
	
	sceneName = getName()
	sceneDir = getDir()
	finalName = ''

	if sceneName.endswith( '.fbx' ):
		sceneName = re.sub('\.fbx$', '', sceneName)
		sceneName += '.ma' 
		finalName = sceneDir +  sceneName

		cmds.file( rename= finalName)
		cmds.file( save=True, type='mayaAscii' )
		OpenMaya.MGlobal.displayInfo('Scene has been saved and renamed.')

	load(finalName)
	OpenMaya.MGlobal.displayInfo('Export successful!')

	
