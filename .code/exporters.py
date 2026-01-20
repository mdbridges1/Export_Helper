# SPDX-License-Identifier: MIT
# Export Helper Pro - Core export functions

import bpy
from .utils import (
    get_exportable_objects,
    get_collection_objects_recursive,
    store_selection,
    restore_selection,
    store_transforms,
    restore_transforms,
    prepare_mesh_for_export,
    cleanup_temp_modifier,
)
from .materials import (
    prepare_materials_for_export,
    cleanup_materials_after_export,
)


def export_fbx_unity(filepath, embed_textures=False):
    """Export FBX with Unity-optimized settings."""
    bpy.ops.export_scene.fbx(
        filepath=filepath,
        check_existing=False,
        use_selection=True,
        use_visible=False,
        use_active_collection=False,
        global_scale=1.0,
        apply_unit_scale=True,
        apply_scale_options='FBX_SCALE_NONE',
        use_space_transform=True,
        bake_space_transform=False,
        object_types={'EMPTY', 'MESH', 'ARMATURE', 'OTHER'},
        use_mesh_modifiers=True,
        use_mesh_modifiers_render=True,
        mesh_smooth_type='FACE',
        use_subsurf=False,
        use_mesh_edges=False,
        use_tspace=True,
        use_triangles=False,
        use_custom_props=False,
        add_leaf_bones=False,
        primary_bone_axis='Y',
        secondary_bone_axis='X',
        use_armature_deform_only=True,
        armature_nodetype='NULL',
        bake_anim=True,
        bake_anim_use_all_bones=True,
        bake_anim_use_nla_strips=True,
        bake_anim_use_all_actions=True,
        bake_anim_force_startend_keying=True,
        bake_anim_step=1.0,
        bake_anim_simplify_factor=1.0,
        path_mode='COPY' if embed_textures else 'AUTO',
        embed_textures=embed_textures,
        batch_mode='OFF',
        axis_forward='-Z',
        axis_up='Y',
    )


def export_fbx_unreal(filepath, embed_textures=False):
    """Export FBX with Unreal-optimized settings."""
    bpy.ops.export_scene.fbx(
        filepath=filepath,
        check_existing=False,
        use_selection=True,
        use_visible=False,
        use_active_collection=False,
        global_scale=1.0,
        apply_unit_scale=True,
        apply_scale_options='FBX_SCALE_NONE',
        use_space_transform=True,
        bake_space_transform=False,
        object_types={'EMPTY', 'MESH', 'ARMATURE', 'OTHER'},
        use_mesh_modifiers=True,
        use_mesh_modifiers_render=True,
        mesh_smooth_type='EDGE',
        use_subsurf=False,
        use_mesh_edges=True,
        use_tspace=True,
        use_triangles=False,
        use_custom_props=False,
        add_leaf_bones=False,
        primary_bone_axis='Y',
        secondary_bone_axis='X',
        use_armature_deform_only=True,
        armature_nodetype='NULL',
        bake_anim=True,
        bake_anim_use_all_bones=True,
        bake_anim_use_nla_strips=True,
        bake_anim_use_all_actions=True,
        bake_anim_force_startend_keying=True,
        bake_anim_step=1.0,
        bake_anim_simplify_factor=1.0,
        path_mode='COPY' if embed_textures else 'AUTO',
        embed_textures=embed_textures,
        batch_mode='OFF',
        axis_forward='-Z',
        axis_up='Y',
    )


def export_fbx_generic(filepath, embed_textures=False):
    """Export FBX with generic settings."""
    bpy.ops.export_scene.fbx(
        filepath=filepath,
        check_existing=False,
        use_selection=True,
        use_visible=False,
        use_active_collection=False,
        global_scale=1.0,
        apply_unit_scale=True,
        apply_scale_options='FBX_SCALE_NONE',
        use_space_transform=True,
        bake_space_transform=True,
        object_types={'EMPTY', 'MESH', 'ARMATURE', 'OTHER'},
        use_mesh_modifiers=True,
        use_mesh_modifiers_render=True,
        mesh_smooth_type='FACE',
        use_subsurf=False,
        use_mesh_edges=False,
        use_tspace=True,
        use_triangles=False,
        use_custom_props=False,
        add_leaf_bones=False,
        primary_bone_axis='Y',
        secondary_bone_axis='X',
        use_armature_deform_only=False,
        armature_nodetype='NULL',
        bake_anim=True,
        bake_anim_use_all_bones=True,
        bake_anim_use_nla_strips=True,
        bake_anim_use_all_actions=True,
        bake_anim_force_startend_keying=True,
        bake_anim_step=1.0,
        bake_anim_simplify_factor=1.0,
        path_mode='COPY' if embed_textures else 'AUTO',
        embed_textures=embed_textures,
        batch_mode='OFF',
        axis_forward='-Z',
        axis_up='Y',
    )


def export_gltf(filepath, gltf_format='GLB'):
    """Export glTF/GLB with proper settings for Blender 4.x/5.x."""
    base_path = filepath.rsplit('.', 1)[0] if '.' in filepath else filepath
    if gltf_format == 'GLB':
        filepath = base_path + '.glb'
    else:
        filepath = base_path + '.gltf'

    try:
        export_params = {
            'filepath': filepath,
            'check_existing': False,
            'use_selection': True,
            'use_visible': False,
            'use_active_collection': False,
            'export_format': gltf_format,
            'export_apply': True,
            'export_texcoords': True,
            'export_normals': True,
            'export_tangents': True,
            'export_materials': 'EXPORT',
            'export_colors': True,
            'export_cameras': False,
            'export_lights': False,
            'export_yup': True,
        }

        if gltf_format == 'GLTF_SEPARATE':
            export_params['export_texture_dir'] = 'textures'
            export_params['export_keep_originals'] = True

        bpy.ops.export_scene.gltf(**export_params)
    except TypeError as e:
        print(f"glTF export - trying minimal parameters due to: {e}")
        try:
            bpy.ops.export_scene.gltf(
                filepath=filepath,
                check_existing=False,
                use_selection=True,
                export_format=gltf_format,
            )
        except Exception as e2:
            print(f"glTF export failed: {e2}")
            raise


def export_obj(filepath):
    """Export OBJ with PBR material extensions."""
    try:
        bpy.ops.wm.obj_export(
            filepath=filepath,
            check_existing=False,
            export_selected_objects=True,
            apply_modifiers=True,
            export_uv=True,
            export_normals=True,
            export_colors=False,
            export_materials=True,
            export_pbr_extensions=True,
            path_mode='AUTO',
            export_triangulated_mesh=False,
            export_curves_as_nurbs=False,
            forward_axis='NEGATIVE_Z',
            up_axis='Y',
        )
    except (AttributeError, TypeError):
        try:
            bpy.ops.wm.obj_export(
                filepath=filepath,
                check_existing=False,
                export_selected_objects=True,
                apply_modifiers=True,
                export_uv=True,
                export_normals=True,
                export_colors=False,
                export_materials=True,
                export_triangulated_mesh=False,
                export_curves_as_nurbs=False,
                forward_axis='NEGATIVE_Z',
                up_axis='Y',
            )
        except AttributeError:
            bpy.ops.export_scene.obj(
                filepath=filepath,
                check_existing=False,
                use_selection=True,
                use_mesh_modifiers=True,
                use_normals=True,
                use_uvs=True,
                use_materials=True,
                use_triangles=False,
                axis_forward='-Z',
                axis_up='Y',
            )


def do_export_single_object(context, obj, export_dir, props):
    """Export a single object. Returns True on success."""
    original_transform = None
    if props.center_origin:
        original_transform = store_transforms(obj)
        obj.location = (0, 0, 0)

    temp_modifier_name = None
    if props.export_format in {'GLTF', 'OBJ'}:
        temp_modifier_name = prepare_mesh_for_export(obj, props.preserve_sharp_edges)

    modified_materials = prepare_materials_for_export([obj], props.convert_viewport_colors)

    selection_state = store_selection(context)

    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)

    if props.include_armatures:
        for mod in obj.modifiers:
            if mod.type == 'ARMATURE' and mod.object:
                mod.object.select_set(True)

    context.view_layer.objects.active = obj

    ext_map = {
        'FBX_UNITY': '.fbx',
        'FBX_UNREAL': '.fbx',
        'FBX_GENERIC': '.fbx',
        'GLTF': '.glb' if props.gltf_format == 'GLB' else '.gltf',
        'OBJ': '.obj',
    }
    ext = ext_map.get(props.export_format, '.fbx')
    filepath = str(export_dir / f"{obj.name}{ext}")

    try:
        if props.export_format == 'FBX_UNITY':
            export_fbx_unity(filepath, props.embed_textures)
        elif props.export_format == 'FBX_UNREAL':
            export_fbx_unreal(filepath, props.embed_textures)
        elif props.export_format == 'FBX_GENERIC':
            export_fbx_generic(filepath, props.embed_textures)
        elif props.export_format == 'GLTF':
            export_gltf(filepath, props.gltf_format)
        elif props.export_format == 'OBJ':
            export_obj(filepath)
        success = True
    except Exception as e:
        print(f"Export failed for {obj.name}: {e}")
        success = False

    cleanup_materials_after_export(modified_materials)

    if temp_modifier_name:
        cleanup_temp_modifier(obj, temp_modifier_name)

    if original_transform:
        restore_transforms(obj, original_transform)

    restore_selection(context, selection_state)

    return success


def do_export_objects(context, objects, export_dir, props):
    """Export multiple objects individually. Returns (success_count, fail_count)."""
    exportable = get_exportable_objects(context, objects)

    success_count = 0
    fail_count = 0

    for obj in exportable:
        if do_export_single_object(context, obj, export_dir, props):
            success_count += 1
        else:
            fail_count += 1

    return success_count, fail_count


def do_export_collection(context, collection, export_dir, props):
    """Export a single collection as one file. Returns (success, error_msg)."""
    all_objects = get_collection_objects_recursive(collection)
    exportable = get_exportable_objects(context, all_objects)

    if not exportable:
        return False, "No exportable objects"

    selection_state = store_selection(context)

    original_transforms = {}
    if props.center_origin:
        for obj in exportable:
            original_transforms[obj.name] = store_transforms(obj)
            obj.location = (0, 0, 0)

    temp_modifiers = {}
    if props.export_format in {'GLTF', 'OBJ'}:
        for obj in exportable:
            mod_name = prepare_mesh_for_export(obj, props.preserve_sharp_edges)
            if mod_name:
                temp_modifiers[obj.name] = mod_name

    modified_materials = prepare_materials_for_export(exportable, props.convert_viewport_colors)

    bpy.ops.object.select_all(action='DESELECT')
    for obj in exportable:
        obj.select_set(True)

    if exportable:
        context.view_layer.objects.active = exportable[0]

    ext_map = {
        'FBX_UNITY': '.fbx',
        'FBX_UNREAL': '.fbx',
        'FBX_GENERIC': '.fbx',
        'GLTF': '.glb' if props.gltf_format == 'GLB' else '.gltf',
        'OBJ': '.obj',
    }
    ext = ext_map.get(props.export_format, '.fbx')
    filepath = str(export_dir / f"{collection.name}{ext}")

    success = True
    error_msg = ""

    try:
        if props.export_format == 'FBX_UNITY':
            export_fbx_unity(filepath, props.embed_textures)
        elif props.export_format == 'FBX_UNREAL':
            export_fbx_unreal(filepath, props.embed_textures)
        elif props.export_format == 'FBX_GENERIC':
            export_fbx_generic(filepath, props.embed_textures)
        elif props.export_format == 'GLTF':
            export_gltf(filepath, props.gltf_format)
        elif props.export_format == 'OBJ':
            export_obj(filepath)
    except Exception as e:
        success = False
        error_msg = str(e)

    cleanup_materials_after_export(modified_materials)

    for obj in exportable:
        if obj.name in temp_modifiers:
            cleanup_temp_modifier(obj, temp_modifiers[obj.name])

    for obj in exportable:
        if obj.name in original_transforms:
            restore_transforms(obj, original_transforms[obj.name])

    restore_selection(context, selection_state)

    return success, error_msg
