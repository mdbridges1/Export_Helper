import bpy
import os
import math

class EXPORT_OT_Operator(bpy.types.Operator):
    bl_idname = "object.exporthelper"
    bl_label = "Export Operator"
    bl_description = "Export GLB OBJ FBX"

    def execute(self, context):
        
        glb_dir = '.\GLB'
        fbx_dir = '.\FBX'
        unity_dir = '.\FBX_Unity'  
        obj_dir = '.\OBJ'
        blend_file_path = bpy.data.filepath
        directory = os.path.dirname(blend_file_path)
         
        bpy.ops.object.select_all(action='DESELECT') 
            
        if os.path.isdir(directory + obj_dir) == False:
            os.makedirs(directory + obj_dir)
            
        if os.path.isdir(directory + fbx_dir) == False:
            os.makedirs(directory + fbx_dir)
            
        if os.path.isdir(directory + glb_dir) == False:
            os.makedirs(directory + glb_dir)

        if os.path.isdir(directory + unity_dir) == False:
            os.makedirs(directory + unity_dir)     

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

        i = 0    
        for i in range(len(bpy.context.scene.objects)):
                
            obj_name = bpy.context.scene.objects[i].name
            bpy.data.objects[obj_name].select_set(True)
            target_file_obj = os.path.join(directory + obj_dir, obj_name + '.obj')

            obj_loc = bpy.data.objects[obj_name].location.copy() # copy location
            bpy.data.objects[obj_name].location = (0,0,0) # move object to world origin

            bpy.ops.export_scene.obj(
                filepath=target_file_obj, 
                check_existing=False, 
                filter_glob="*.obj;*.mtl", 
                use_selection=True, 
                use_animation=False, 
                use_mesh_modifiers=True, 
                use_edges=True, 
                use_smooth_groups=False, 
                use_smooth_groups_bitflags=False, 
                use_normals=True, 
                use_uvs=True, 
                use_materials=True, 
                use_triangles=False, 
                use_nurbs=False, 
                use_vertex_groups=False, 
                use_blen_objects=True, 
                group_by_object=False, 
                group_by_material=False, 
                keep_vertex_order=False, 
                global_scale=1, 
                path_mode='AUTO', 
                axis_forward='-Z', 
                axis_up='Y')
             
            bpy.data.objects[obj_name].location = obj_loc # set object back to it's original location    
            bpy.ops.object.select_all(action='DESELECT')   
            i =+ 1
            
        i = 0    
        for i in range(len(bpy.context.scene.objects)):
            
            obj_name = bpy.context.scene.objects[i].name
            bpy.data.objects[obj_name].select_set(True)
            target_file_fbx = os.path.join(directory + fbx_dir, obj_name + '.fbx')

            obj_loc = bpy.data.objects[obj_name].location.copy() # copy location
            bpy.data.objects[obj_name].location = (0,0,0) # move object to world origin
            
            bpy.ops.export_scene.fbx(
                filepath=target_file_fbx, 
                check_existing=False, 
                filter_glob="*.fbx", 
                use_selection=True, 
                use_active_collection=False, 
                global_scale=1, 
                apply_unit_scale=True, 
                apply_scale_options='FBX_SCALE_NONE', 
                bake_space_transform=False, 
                object_types={'EMPTY', 'CAMERA', 'LIGHT', 'ARMATURE', 'MESH', 'OTHER'}, 
                use_mesh_modifiers=True, 
                use_mesh_modifiers_render=True, 
                mesh_smooth_type='OFF', 
                use_subsurf=False, 
                use_mesh_edges=False, 
                use_tspace=False, 
                use_custom_props=False, 
                add_leaf_bones=True, 
                primary_bone_axis='Y', 
                secondary_bone_axis='X', 
                use_armature_deform_only=False, 
                armature_nodetype='NULL', 
                bake_anim=True, 
                bake_anim_use_all_bones=True, 
                bake_anim_use_nla_strips=True, 
                bake_anim_use_all_actions=True, 
                bake_anim_force_startend_keying=True, 
                bake_anim_step=1, 
                bake_anim_simplify_factor=1, 
                path_mode='AUTO', 
                embed_textures=False, 
                batch_mode='OFF', 
                use_batch_own_dir=True, 
                use_metadata=True, 
                axis_forward='-Z', 
                axis_up='Y')
            
            bpy.data.objects[obj_name].location = obj_loc # set object back to it's original location
            bpy.ops.object.select_all(action='DESELECT')   
            i =+ 1

        # Unity Specific Export Settings and Code
        i = 0    
        for i in range(len(bpy.context.scene.objects)):
            
            obj_name = bpy.context.scene.objects[i].name
            bpy.data.objects[obj_name].select_set(True)
            target_file_fbx = os.path.join(directory + unity_dir, obj_name + '.fbx')

            # Unity Faff
            # Prevents, error - need to warn user
            bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', object=True, obdata=True)

            # Would prefer to set_rotation? if possible.
            bpy.ops.transform.rotate(value = math.pi, orient_axis='Z', orient_type='GLOBAL')
            bpy.ops.transform.rotate(value = (math.pi / 2), orient_axis='X', orient_type='GLOBAL')
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

            bpy.ops.transform.rotate(value = (-math.pi / 2), orient_axis='X', orient_type='GLOBAL')

            obj_loc = bpy.data.objects[obj_name].location.copy() # copy location
            bpy.data.objects[obj_name].location = (0,0,0) # move object to world origin
            
            bpy.ops.export_scene.fbx(
                filepath=target_file_fbx, 
                check_existing=False, 
                filter_glob="*.fbx", 
                use_selection=True, 
                use_active_collection=False, 
                global_scale=1, 
                apply_unit_scale=True, 
                apply_scale_options='FBX_SCALE_NONE', 
                bake_space_transform=False, 
                object_types={'EMPTY', 'CAMERA', 'LIGHT', 'ARMATURE', 'MESH', 'OTHER'}, 
                use_mesh_modifiers=True, 
                use_mesh_modifiers_render=True, 
                mesh_smooth_type='OFF', 
                use_subsurf=False, 
                use_mesh_edges=False, 
                use_tspace=False, 
                use_custom_props=False, 
                add_leaf_bones=True, 
                primary_bone_axis='Y', 
                secondary_bone_axis='X', 
                use_armature_deform_only=False, 
                armature_nodetype='NULL', 
                bake_anim=True, 
                bake_anim_use_all_bones=True, 
                bake_anim_use_nla_strips=True, 
                bake_anim_use_all_actions=True, 
                bake_anim_force_startend_keying=True, 
                bake_anim_step=1, 
                bake_anim_simplify_factor=1, 
                path_mode='AUTO', 
                embed_textures=False, 
                batch_mode='OFF', 
                use_batch_own_dir=True, 
                use_metadata=True, 
                axis_forward='-Z', 
                axis_up='Y')

            ## More Unity Faff, putting objects back to original state for user.
            bpy.ops.transform.rotate(value = math.pi, orient_axis='Z', orient_type='GLOBAL')
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
            
            bpy.data.objects[obj_name].location = obj_loc # set object back to it's original location
            bpy.ops.object.select_all(action='DESELECT')   
            i =+ 1
            
        return {'FINISHED'}