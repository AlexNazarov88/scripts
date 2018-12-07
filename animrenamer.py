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

# personage file name templates
KARL = "karl_skeleton.2_anims_"
KARL_ITEM = "karl_item_"
AMELIA = "amelia_skeleton.2_anims_"
AMELIA_ITEM = "amelia_items_"

animFileName = ''
currPreset = ''
textField = ''
# add variables to hold text strings

def UI():

    # if cmds.window( "renamerUI", exists=True ):
    #     cmds.showWindow("renamerUI")
    #     return
    
    window = cmds.window( "renamerUI", title="animations file renamer", widthHeight=(100, 150))

    cmds.columnLayout(adjustableColumn=True, columnOffset=("both", 2))

    cmds.separator(style = "none", height = 15)
    cmds.rowColumnLayout( numberOfColumns=2, columnWidth=[(1, 180), (2, 200)])
    cmds.optionMenu( label='Preset', changeCommand = selectPreset )
    cmds.menuItem( label='karl', command = selectPreset)
    cmds.menuItem( label='karl_item', command = selectPreset )
    cmds.menuItem( label='amelia', command = selectPreset )
    cmds.menuItem( label='amelia_items', command = selectPreset )
    # cmds.separator(style = "none", width = 5)
    cmds.textField("newFileName", text = textField, changeCommand = onNewFileNameChanged)
    cmds.setParent("..")

    cmds.separator(style = "none", height = 15)

    cmds.button("OkButton", label = "Ok", command = renameAnimFile)

    cmds.showWindow("renamerUI")


def selectPreset(arg):
    global currPreset
    # global KARL
    # global KARL_ITEM
    # global AMELIA
    # global AMELIA_ITEM

    currPreset = arg
    # print currPreset
    # if currPreset == 'karl':
    #     onNewFileNameChanged(KARL)
    # elif currPreset == 'karl_item':
    #     onNewFileNameChanged(KARL_ITEM)
    # elif currPreset == 'amelia':
    #     onNewFileNameChanged(AMELIA)
    # elif currPreset == 'amelia_items':
    #     onNewFileNameChanged(AMELIA_ITEM)
    # else:
    #     print "Preset not implemented yet" # maybe not needed


def onNewFileNameChanged(arg):
    print "onNewFileNameChanged " + arg
    global textField
    textField = arg


def renameAnimFile(arg):
    # currPreset + textField? = animFileName
    dasdasd=''


def getFile(arg):
    ddsadasd=''