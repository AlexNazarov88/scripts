#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Oleksandr Nazarov - aleksandr.nazarov@vokigames.com
# Voki Games
#
# This script needs to be added to:
# C:/Users/*Your User*/Documents/maya/2018/scripts
# usage:
#
#     In Maya, select needed bones/transformations/groups and run in script editor
#
#     run selectively:
#         import mayatoxml
#         mayatoxml.factory()
#     run all:
#         import mayatoxml
#         mayatoxml.factory(True)

import timingsfix
from time import localtime, strftime
import os
import argparse
import cvxporter2 as xporter
import maya.OpenMayaAnim as OpenMayaAnim
import maya.OpenMaya as OpenMaya
import maya.cmds as cmds
import sys

sys.dont_write_bytecode = True
DEFAULTANIMFILE = "timing.txt"

# def getProjName():
#     # gets the name of maya project file
#     return projName.lower() # lower() may be needed as project name sometimes comes in capitals
#     projName = cmds.workspace(shortName = True)


def getAnimsFile():
    global DEFAULTANIMFILE
    sceneDir = os.path.dirname(cmds.file(location=True, query=True)) + "/"
    timingsFile = sceneDir + DEFAULTANIMFILE
    try:
        if not os.path.exists(timingsFile):
            raise Exception
    except Exception:
        OpenMaya.MGlobal.displayError('Timings file does not exist.' + str(Exception.message))
    return timingsFile


def createXML():
    sceneDir = os.path.dirname(cmds.file(location=True, query=True)) + "/"
    fileName = sceneDir + 'export_' + strftime("%d-%m-%Y_%H%M%S", localtime())
    if not fileName.endswith('.xml'):
        fileName += '.xml'
    file = open(fileName, 'w') # replace file creation logic (with...)
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


def runAllExport():
    # need to add error handling - try except
    OpenMaya.MGlobal.displayInfo('Starting export everything...')
    xporter.doExport(True)


def factory(all=False):
    # main function
    OpenMaya.MGlobal.displayInfo('Running Maya to XML export script')
    OpenMaya.MGlobal.displayInfo('Preparing export...')

    xmlFile = ''
    xmlFile = createXML()
    setXMLFile(xmlFile)
    # to do: improve animation timings file check up
    animFile = ''
    animFile = getAnimsFile()
    timingsfix.fixTiming()
    setAnimFile(animFile)
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