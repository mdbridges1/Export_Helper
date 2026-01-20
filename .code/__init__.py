# SPDX-License-Identifier: MIT
# Export Helper Pro - Batch export for FBX, glTF, OBJ with engine presets

bl_info = {
    "name": "Export Helper Pro",
    "author": "Michael Bridges (original Export_Helper), Embark Studios (inspiration), Combined Edition",
    "version": (2, 0, 0),
    "blender": (4, 2, 0),
    "location": "View3D > Sidebar > Export Helper",
    "description": "Batch export objects/collections to FBX, glTF, OBJ with presets for Unity, Unreal, and Godot",
    "warning": "",
    "doc_url": "https://github.com/mdbridges1/Export_Helper",
    "category": "Import-Export",
}

import bpy
from bpy.props import PointerProperty

from .properties import (
    ExportCollectionItem,
    ExportHelperProperties,
)
from .operators import (
    EXPORT_HELPER_OT_export_all,
    EXPORT_HELPER_OT_export_selected,
    EXPORT_HELPER_OT_export_collection,
    EXPORT_HELPER_OT_add_collection,
    EXPORT_HELPER_OT_remove_collection,
    EXPORT_HELPER_OT_add_all_collections,
    EXPORT_HELPER_OT_export_multi_collections,
    EXPORT_HELPER_OT_open_export_folder,
)
from .panel import (
    EXPORT_HELPER_UL_collections,
    EXPORT_HELPER_PT_main_panel,
)

classes = (
    ExportCollectionItem,
    ExportHelperProperties,
    EXPORT_HELPER_OT_export_all,
    EXPORT_HELPER_OT_export_selected,
    EXPORT_HELPER_OT_export_collection,
    EXPORT_HELPER_OT_add_collection,
    EXPORT_HELPER_OT_remove_collection,
    EXPORT_HELPER_OT_add_all_collections,
    EXPORT_HELPER_OT_export_multi_collections,
    EXPORT_HELPER_OT_open_export_folder,
    EXPORT_HELPER_UL_collections,
    EXPORT_HELPER_PT_main_panel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.export_helper_props = PointerProperty(type=ExportHelperProperties)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.export_helper_props


if __name__ == "__main__":
    register()
