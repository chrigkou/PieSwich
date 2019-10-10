import bpy

class Pie_Switcher_Menu(bpy.types.Menu):
    bl_idname = "Pie_Switcher_Menu"
    bl_label = "Fase Workspace Switch"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        pie.operator('view3d.cursor_center', text = "changemotherfucker").id = 0
        pie.operator('view3d.cursor_center', text = "changelayout").id = 1
        
    

