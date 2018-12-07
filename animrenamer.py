"""
Author: Oleksandr Nazarov - aleksandr.nazarov@vokigames.com
Voki Games

This script needs to be added to:
C:/Users/*Your User*/Documents/maya/2016/scripts
usage:
    

    
"""


import sys
sys.dont_write_bytecode = True

import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as OpenMaya
# import maya.OpenMayaAnim as OpenMayaAnim
import os
import glob

# personage file name templates
KARL = "karl_skeleton.2_anims_"
KARL_ITEM = "karl_item_"
AMELIA = "amelia_skeleton.2_anims_"
AMELIA_ITEM = "amelia_items_"

resultFileName = ''
fileName = ''
currPreset = ''
animName = ''


# добавить еще селектор с выбором файлов в папке (xml)
# how to get files to rename?

def UI(file):

    # if cmds.window( "renamerUI", exists=True ):
    #     cmds.showWindow("renamerUI")
    #     return
    
    window = cmds.window( "renamerUI", title="animations file renamer", widthHeight=(180, 200))

    cmds.columnLayout(adjustableColumn=True, columnOffset=("both", 2))

    cmds.separator(style = "none", height = 15)
    cmds.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 180), (2, 200)])
    cmds.optionMenu( label='Preset', changeCommand = selectPreset )
    cmds.menuItem( label='karl', command = selectPreset)
    cmds.menuItem( label='karl_item', command = selectPreset )
    cmds.menuItem( label='amelia', command = selectPreset )
    cmds.menuItem( label='amelia_items', command = selectPreset )
    # cmds.separator(style = "none", width = 5)
    cmds.textField("newFileName", text = animName, changeCommand = onNewFileNameChanged)
    cmds.setParent("..")

    cmds.separator(style = "none", height = 15)

    cmds.button("OkButton", label = "Ok", command = renameAnimFile)

    # getFile(file)
    cmds.showWindow("renamerUI")


def selectPreset(arg):
    global currPreset
    if arg == 'karl':
        currPreset = KARL
    elif arg == 'karl_item':
        currPreset = KARL_ITEM
    elif arg == 'amelia':
        currPreset = AMELIA
    elif arg == 'amelia_items':
        currPreset = AMELIA_ITEM
    print currPreset


def onNewFileNameChanged(arg):
    print "onNewFileNameChanged " + arg
    global animName
    animName = arg


def renameAnimFile(arg):
    # currPreset + animName? = animFileName
    global resultFileName
    global currPreset
    global animName
    global fileName       
    # global KARL
    # global KARL_ITEM
    # global AMELIA
    # global AMELIA_ITEM

    resultFileName = currPreset + animName
    print "Before rename: " + resultFileName
    os.rename(fileName, resultFileName)
    print "After rename: " + resultFileName


def getFiles(arg):
    # global fileName
    # fileName = arg
    foundFiles = glob.glob("/*.xml") 
    return foundFiles