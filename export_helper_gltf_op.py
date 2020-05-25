import bpy
import os
import math

class EXPORTGLB_OT_Operator(bpy.types.Operator):

    bl_idname = "object.export_gltf"
    bl_label = "Export Operator"
    bl_description = "Export GLB"

    def execute(self, context):
        
        glb_dir = '.\GLB'
        blend_file_path = bpy.data.filepath
        directory = os.path.dirname(blend_file_path)
        
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.select_all(action='DESELECT') 
     
        if os.path.isdir(directory + glb_dir) == False:
            os.makedirs(directory + glb_dir)   

        i = 0
        for i in range(len(bpy.context.scene.objects)):
                
            obj_name = bpy.context.scene.objects[i].name
            target_file_glb = os.path.join(directory + glb_dir, obj_name)
            bpy.data.objects[obj_name].select_set(True)

            obj_loc = bpy.data.objects[obj_name].location.copy() # copy location
            bpy.data.objects[obj_name].location = (0,0,0) # move object to world origin

            bpy.ops.export_scene.gltf(
                export_format='GLB', 
                ui_tab='GENERAL', 
                export_copyright="Michael Bridges", 
                export_image_format='PNG', 
                export_texture_dir="", 
                export_texcoords=True, 
                export_normals=True, 
                export_draco_mesh_compression_enable=False, 
                export_draco_mesh_compression_level=6, 
                export_draco_position_quantization=14, 
                export_draco_normal_quantization=10, 
                export_draco_texcoord_quantization=12, 
                export_draco_generic_quantization=12, 
                export_tangents=False, 
                export_materials=True, 
                export_colors=True, 
                export_cameras=False, 
                export_selected=True, 
                export_extras=False, 
                export_yup=True, 
                export_apply=True, 
                export_animations=True, 
                export_frame_range=True, 
                export_frame_step=1, 
                export_force_sampling=True, 
                export_nla_strips=True, 
                export_def_bones=False, 
                export_current_frame=False, 
                export_skins=True, 
                export_all_influences=False, 
                export_morph=True, 
                export_morph_normal=True, 
                export_morph_tangent=False, 
                export_lights=False,  
                export_displacement=False, 
                will_save_settings=True, 
                filepath=target_file_glb, 
                check_existing=True, 
                filter_glob="*.glb;*.gltf")

            bpy.data.objects[obj_name].location = obj_loc # set object back to it's original location
            bpy.ops.object.select_all(action='DESELECT')   
            i =+ 1

        return {'FINISHED'}

class EXPORTGLBALL_OT_Operator(bpy.types.Operator):

    bl_idname = "object.export_gltf_all"
    bl_label = "Export Operator"
    bl_description = "Export GLB"

    def execute(self, context):
        
        glb_dir = '.\GLB'
        blend_file_path = bpy.data.filepath
        directory = os.path.dirname(blend_file_path)
        obj_list = bpy.context.scene.objects
        obj_locs = {} # dictionary ready for objects locations

        obj_name = str(bpy.path.basename(bpy.context.blend_data.filepath))    
        target_file_glb = os.path.join(directory + glb_dir, obj_name)
        
        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.select_all(action='DESELECT') 
     
        if os.path.isdir(directory + glb_dir) == False:
            os.makedirs(directory + glb_dir)   

        i = 0
        for i in range(len(obj_list)):
            name = bpy.data.objects[i].name
            bpy.data.objects[name].select_set(True)
            obj_locs[i] = (bpy.data.objects[i].location.copy()) # copy locations of objects
            bpy.data.objects[i].location = (0,0,0) # move object to world origin
            i += 1

        bpy.ops.export_scene.gltf(
            export_format='GLB', 
            ui_tab='GENERAL', 
            export_copyright="Michael Bridges", 
            export_image_format='PNG', 
            export_texture_dir="", 
            export_texcoords=True, 
            export_normals=True, 
            export_draco_mesh_compression_enable=False, 
            export_draco_mesh_compression_level=6, 
            export_draco_position_quantization=14, 
            export_draco_normal_quantization=10, 
            export_draco_texcoord_quantization=12, 
            export_draco_generic_quantization=12, 
            export_tangents=False, 
            export_materials=True, 
            export_colors=True, 
            export_cameras=False, 
            export_selected=True, 
            export_extras=False, 
            export_yup=True, 
            export_apply=True, 
            export_animations=True, 
            export_frame_range=True, 
            export_frame_step=1, 
            export_force_sampling=True, 
            export_nla_strips=True, 
            export_def_bones=False, 
            export_current_frame=False, 
            export_skins=True, 
            export_all_influences=False, 
            export_morph=True, 
            export_morph_normal=True, 
            export_morph_tangent=False, 
            export_lights=False,  
            export_displacement=False, 
            will_save_settings=True, 
            filepath=target_file_glb, 
            check_existing=True, 
            filter_glob="*.glb;*.gltf")

        i = 0
        for i in range(len(obj_list)):
            bpy.data.objects[i].location = obj_locs[i] # set object back to it's original location
            i =+ 1

        bpy.ops.object.select_all(action='DESELECT')   

        return {'FINISHED'}