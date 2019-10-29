import bpy

class Pie_Switcher_Menu(bpy.types.Menu):
    bl_idname = "Pie_Switcher_Menu"
    bl_label = "Workspace Switch"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator('view3d.cursor_center', text = "Layout").id = 1
        pie.operator('view3d.cursor_center', text = "Modeling").id = 2
        pie.operator('view3d.cursor_center', text = "Shading").id = 3
        pie.operator('view3d.cursor_center', text = "Sculpting").id = 0
        pie.operator('view3d.cursor_center', text = "UV Editing").id = 4
        pie.operator('view3d.cursor_center', text = "Texture Paint").id = 5
        pie.operator('view3d.cursor_center', text = "Animation").id = 6
        pie.operator('view3d.cursor_center', text = "Scripting").id = 7  

