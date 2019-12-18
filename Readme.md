# PieSwitcher blender addon

**PieSwitcher** is a blender addon the allows you to switch between workspaces using a pie menu. It's default shortcut key is **TAB** 


## How to install

 1. Download as **zip** from github 
 2. Open blender and go edit->preferences->addons
 3. Select install and choose the zip file 

## How to use 

There are **2 ways** to use it. First, in any workspace go to the **3D Viewport** and press **TAB** , select the workspace to switch to and left click.
The Second way, is instead of pressing tab to **hold it**, move the mouse in the direction of the workspace you want and release to switch

## Project structure

 - pie_switcher.py builds the menu and adds the items
 - first_op.py contains the operator that executes the switch
 - \_\_init\_\_.py registers the classes and the buttons and contains metadata
