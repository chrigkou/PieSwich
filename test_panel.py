import bpy
 
class Test_pt_Panel(bpy.types.Panel):
    bl_idname= "Test_pt_Panel"
    bl_label = "Test p"
    bl_category = "Test Addon"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
 
 
    def draw(self, context):
        layout = self.layout
 
        row = layout.row()
        row.operator('view3d.cursor_center', text = "changemotherfucker").id = 0
        row.operator('view3d.cursor_center', text = "changelayout").id = 1