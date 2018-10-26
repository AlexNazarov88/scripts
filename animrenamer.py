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
# import maya.mel as mel
import maya.OpenMaya as OpenMaya
# import maya.OpenMayaAnim as OpenMayaAnim
import os

# personage file name templates
KARL = "karl_skeleton.2_anims_"
KARL_ITEM = "karl_item_"
AMELIA = "amelia_skeleton.2_anims_"
AMELIA_ITEM = "amelia_items_"

animFileName = ''


def UI():

    if cmds.window( "renamerUI", exists=True ):
        cmds.showWindow("renamerUI")
        return
    
    window = cmds.window( "renamerUI", title="animations file renamer", resizeToFitChildren = True, widthHeight=(250, 250))
    cmds.columnLayout()
    cmds.optionMenu( label='presets', changeCommand = selectPreset )
    cmds.menuItem( label='karl' )
    cmds.menuItem( label='karl_item' )
    cmds.menuItem( label='amelia' )
    cmds.menuItem( label='amelia_items' )
    cmds.textField("newFileName", text = "", changeCommand = onNewFileNameChanged)
    cmds.setParent("..")

    cmds.separator(style = "none", height = 15)
    cmds.button("OkButton", label = "Ok", command = renameAnimFile)

    cmds.showWindow(window)

def selectPreset(arg):
    animFileName = ''
    animFileName += arg

def onNewFileNameChanged():
    dasdasd=''

def renameAnimFile():
    dasdasd=''
