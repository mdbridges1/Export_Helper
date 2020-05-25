import bpy

class EXPORT_PT_Panel(bpy.types.Panel):
    bl_idname = "object.export_gltf"
    bl_label = "Export Helper"
    bl_category = "Export Helper"
    bl_space_type = "VIEW_3D"    #important for Blender 2.8
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        box = layout.box()
        row = box.row()
        row.label(text = "Center And Export")
        row = box.row()
        row.label(text = "All Objects Individually")
        row = box.row()
        row.operator('object.export_gltf', text = "Individual GLB")
        row = box.row()
        row.operator('object.export_obj', text = "Individual OBJ")
        row = box.row()
        row.operator('object.export_fbx', text = "Individual FBX")
        row = box.row()
        row.operator('object.export_unityfbx', text = "Individual FBX for Unity")

        box = layout.box()
        row = box.row()
        row.label(text = "Center And Export")
        row = box.row()
        row.label(text = "All Objects As One File")
        row = box.row()
        row.operator('object.export_gltf_all', text = "AIO GLB")
