import bpy

class EXPORT_PT_Panel(bpy.types.Panel):
    bl_idname = "object.export_gltf"
    bl_label = "Export Helper"
    bl_category = "Export Helper"
    bl_space_type = "VIEW_3D"    #important for Blender 2.8
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator('object.export_gltf', text = "Export GLB")

        row = layout.row()
        row.operator('object.export_obj', text = "Export OBJ")

        row = layout.row()
        row.operator('object.export_fbx', text = "Export FBX")

        row = layout.row()
        row.operator('object.export_unityfbx', text = "Export FBX for Unity")