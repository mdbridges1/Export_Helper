# SPDX-License-Identifier: MIT
# Export Helper Pro - Utility functions

import bpy
from pathlib import Path


def get_blend_filename():
    """Get the blend file name without extension."""
    if not bpy.data.filepath:
        return None
    return Path(bpy.data.filepath).stem


def get_export_path(context):
    """Get or create export folder next to the .blend file."""
    blend_path = bpy.data.filepath
    if not blend_path:
        return None

    blend_dir = Path(blend_path).parent
    blend_name = Path(blend_path).stem
    props = context.scene.export_helper_props

    format_folders = {
        'FBX_UNITY': 'FBX_Unity',
        'FBX_UNREAL': 'FBX_Unreal',
        'FBX_GENERIC': 'FBX',
        'GLTF': 'GLB' if props.gltf_format == 'GLB' else 'glTF',
        'OBJ': 'OBJ',
    }

    subfolder = format_folders.get(props.export_format, 'Exports')
    export_dir = blend_dir / f"{blend_name}-export" / subfolder
    export_dir.mkdir(parents=True, exist_ok=True)

    return export_dir


def get_exportable_objects(context, objects):
    """Filter objects to only exportable types (mesh, armature, empty, curve)."""
    exportable_types = {'MESH', 'ARMATURE', 'EMPTY', 'CURVE', 'SURFACE', 'FONT'}
    return [obj for obj in objects if obj.type in exportable_types]


def get_collection_objects_recursive(collection):
    """Get all objects from a collection and its sub-collections recursively."""
    objects = list(collection.objects)
    for child_collection in collection.children:
        objects.extend(get_collection_objects_recursive(child_collection))
    return objects


def count_subcollections_recursive(collection):
    """Count total sub-collections recursively."""
    count = len(collection.children)
    for child in collection.children:
        count += count_subcollections_recursive(child)
    return count


def store_selection(context):
    """Store current selection state."""
    return {
        'active': context.view_layer.objects.active,
        'selected': [obj for obj in context.selected_objects],
    }


def restore_selection(context, state):
    """Restore selection state."""
    bpy.ops.object.select_all(action='DESELECT')
    for obj in state['selected']:
        if obj.name in bpy.data.objects:
            obj.select_set(True)
    if state['active'] and state['active'].name in bpy.data.objects:
        context.view_layer.objects.active = state['active']


def store_transforms(obj):
    """Store object transform for restoration."""
    return {
        'location': obj.location.copy(),
    }


def restore_transforms(obj, transforms):
    """Restore object transform."""
    obj.location = transforms['location']


def prepare_mesh_for_export(obj, preserve_sharp=True):
    """Add temporary Edge Split modifier if mesh has sharp edges but no such modifier.

    Returns the modifier name if one was added, None otherwise.
    """
    if not preserve_sharp or obj.type != 'MESH':
        return None

    mesh = obj.data
    has_sharp_edges = any(edge.use_edge_sharp for edge in mesh.edges)

    if not has_sharp_edges:
        return None

    for mod in obj.modifiers:
        if mod.type == 'EDGE_SPLIT':
            return None

    mod = obj.modifiers.new(name="_TempEdgeSplit", type='EDGE_SPLIT')
    mod.use_edge_angle = False
    mod.use_edge_sharp = True
    return mod.name


def cleanup_temp_modifier(obj, mod_name):
    """Remove temporary modifier added for export."""
    if mod_name and obj and mod_name in obj.modifiers:
        obj.modifiers.remove(obj.modifiers[mod_name])
