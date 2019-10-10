import bpy

class Test_pie(bpy.types.Operator):
    bl_idname = "view3d.cursor_center"
    bl_label = "Simple operator"
    bl_description = "Center 3d cursor"

    id = bpy.props.IntProperty(default=0)
    output = ['Sculpting',
            'Layout']

    def execute(self, context):
        #layout = self.layout
        context.window.workspace = bpy.data.workspaces[self.output[self.id]]
        return {'FINISHED'}

        