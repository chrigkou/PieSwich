# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "PieSwitcher",
    "author" : "Christina,Dimitris",
    "description" : "Simple pie addon",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from bpy.props import *
from bpy.types import AddonPreferences
import rna_keymap_ui

from . first_op import Test_pie
from . test_panel import Test_pt_Panel
from . pie_switcher import Pie_Switcher_Menu

def register():
    bpy.utils.register_class(Test_pie)
    bpy.utils.register_class(Test_pt_Panel)
    bpy.utils.register_class(Pie_Switcher_Menu)

    kc = bpy.context.window_manager.keyconfigs.addon
    kn = kc.keymaps.new(name='3D View', space_type='VIEW_3D')

    kni = kn.keymap_items.new("wm.call_menu_pie", "COMMA", "PRESS", shift=True)
    kni.properties.name = Pie_Switcher_Menu.bl_idname
    addon_keymaps.append((kn, kni))

def unregister():
    bpy.utils.unregister_class(Test_pt_Panel)
    bpy.utils.unregister_class(Test_pie)
    bpy.utils.unregister_class(Pie_Switcher_Menu)