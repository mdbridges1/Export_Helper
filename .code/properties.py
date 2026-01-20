# SPDX-License-Identifier: MIT
# Export Helper Pro - Property definitions

import bpy
from bpy.props import (
    BoolProperty,
    EnumProperty,
    PointerProperty,
    CollectionProperty,
    IntProperty,
)
from bpy.types import PropertyGroup


class ExportCollectionItem(PropertyGroup):
    """Item in the collection export list."""
    collection: PointerProperty(
        name="Collection",
        type=bpy.types.Collection,
    )
    export_enabled: BoolProperty(
        name="Export",
        default=True,
    )


class ExportHelperProperties(PropertyGroup):
    """Addon properties stored on the scene."""

    export_format: EnumProperty(
        name="Export Format",
        description="Choose export format and preset",
        items=[
            ('FBX_UNITY', "FBX (Unity)", "FBX optimized for Unity"),
            ('FBX_UNREAL', "FBX (Unreal)", "FBX optimized for Unreal Engine"),
            ('FBX_GENERIC', "FBX (Generic)", "FBX with standard settings"),
            ('GLTF', "glTF/GLB", "glTF 2.0 binary format (Godot, web, etc.)"),
            ('OBJ', "OBJ", "Wavefront OBJ format"),
        ],
        default='FBX_UNITY',
    )

    center_origin: BoolProperty(
        name="Center Origins",
        description="Temporarily move objects to world origin for export",
        default=True,
    )

    include_armatures: BoolProperty(
        name="Include Armatures",
        description="Include armature when exporting rigged meshes",
        default=True,
    )

    embed_textures: BoolProperty(
        name="Embed Textures",
        description="Embed textures inside FBX file (increases file size but more portable)",
        default=False,
    )

    preserve_sharp_edges: BoolProperty(
        name="Preserve Sharp Edges",
        description="Temporarily apply Edge Split modifier to preserve flat shading (glTF/OBJ)",
        default=True,
    )

    convert_viewport_colors: BoolProperty(
        name="Convert Viewport Colours",
        description="Create Principled BSDF materials from Viewport Display colours for export",
        default=True,
    )

    gltf_format: EnumProperty(
        name="glTF Format",
        description="Choose glTF export format",
        items=[
            ('GLB', "GLB (Binary)", "Single binary file with embedded textures"),
            ('GLTF_SEPARATE', "glTF + Files", "Separate .gltf, .bin, and texture files"),
        ],
        default='GLB',
    )

    target_collection: PointerProperty(
        name="Target Collection",
        description="Collection to export (includes all sub-collections)",
        type=bpy.types.Collection,
    )

    export_collections: CollectionProperty(
        name="Export Collections",
        type=ExportCollectionItem,
    )

    active_collection_index: IntProperty(
        name="Active Collection Index",
        default=0,
    )
