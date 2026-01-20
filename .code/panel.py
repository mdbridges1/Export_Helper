# SPDX-License-Identifier: MIT
# Export Helper Pro - UI panel and UIList

import bpy
from bpy.types import Panel, UIList
from .utils import (
    get_blend_filename,
    get_exportable_objects,
    get_collection_objects_recursive,
    count_subcollections_recursive,
)


class EXPORT_HELPER_UL_collections(UIList):
    """UI List for displaying collections to export."""
    bl_idname = "EXPORT_HELPER_UL_collections"

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            row = layout.row(align=True)
            row.prop(item, "export_enabled", text="")

            if item.collection:
                row.prop(item, "collection", text="", emboss=False, icon='OUTLINER_COLLECTION')
                obj_count = len(get_exportable_objects(context, get_collection_objects_recursive(item.collection)))
                row.label(text=f"({obj_count})")
            else:
                row.label(text="(Select Collection)", icon='ERROR')

        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            layout.label(text="", icon='OUTLINER_COLLECTION')


class EXPORT_HELPER_PT_main_panel(Panel):
    """Main panel in the 3D View sidebar"""
    bl_label = "Export Helper Pro"
    bl_idname = "EXPORT_HELPER_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Export"

    def draw(self, context):
        layout = self.layout
        props = context.scene.export_helper_props

        if not bpy.data.filepath:
            box = layout.box()
            box.alert = True
            box.label(text="Save .blend file first!", icon='ERROR')
            return

        layout.label(text="Export Format:", icon='EXPORT')
        layout.prop(props, "export_format", text="")

        layout.separator()
        layout.label(text="Options:", icon='PREFERENCES')
        layout.prop(props, "center_origin")
        layout.prop(props, "convert_viewport_colors")

        if props.export_format.startswith('FBX'):
            layout.prop(props, "include_armatures")
            layout.prop(props, "embed_textures")
        elif props.export_format == 'GLTF':
            layout.prop(props, "gltf_format")
            layout.prop(props, "preserve_sharp_edges")
        elif props.export_format == 'OBJ':
            layout.prop(props, "preserve_sharp_edges")

        layout.separator()
        layout.label(text="Object Export:", icon='MESH_DATA')

        row = layout.row(align=True)
        row.scale_y = 1.5
        row.operator("export_helper.export_all", icon='WORLD')

        row = layout.row(align=True)
        row.scale_y = 1.2
        row.operator("export_helper.export_selected", icon='RESTRICT_SELECT_OFF')

        layout.separator()
        box = layout.box()
        box.label(text="Quick Collection Export:", icon='OUTLINER_COLLECTION')
        box.prop(props, "target_collection", text="")

        if props.target_collection:
            subcol_count = count_subcollections_recursive(props.target_collection)
            obj_count = len(get_exportable_objects(context, get_collection_objects_recursive(props.target_collection)))
            if subcol_count > 0:
                box.label(text=f"  {obj_count} objects in {subcol_count + 1} collections", icon='INFO')
            else:
                box.label(text=f"  {obj_count} objects", icon='INFO')

        row = box.row()
        row.enabled = props.target_collection is not None
        row.operator("export_helper.export_collection", icon='EXPORT')

        layout.separator()
        box = layout.box()
        box.label(text="Multi-Collection Export:", icon='OUTLINER')

        row = box.row()
        row.template_list(
            "EXPORT_HELPER_UL_collections", "",
            props, "export_collections",
            props, "active_collection_index",
            rows=3,
        )

        col = row.column(align=True)
        col.operator("export_helper.add_collection", icon='ADD', text="")
        col.operator("export_helper.remove_collection", icon='REMOVE', text="")
        col.separator()
        col.operator("export_helper.add_all_collections", icon='PRESET_NEW', text="")

        enabled_count = sum(1 for item in props.export_collections if item.export_enabled and item.collection)
        row = box.row()
        row.scale_y = 1.3
        row.enabled = enabled_count > 0
        row.operator("export_helper.export_multi_collections",
                     text=f"Export {enabled_count} Collection{'s' if enabled_count != 1 else ''}",
                     icon='EXPORT')

        layout.separator()
        layout.operator("export_helper.open_folder", icon='FILE_FOLDER')

        layout.separator()
        box = layout.box()
        box.scale_y = 0.8
        blend_name = get_blend_filename()
        if blend_name:
            format_folders = {
                'FBX_UNITY': 'FBX_Unity',
                'FBX_UNREAL': 'FBX_Unreal',
                'FBX_GENERIC': 'FBX',
                'GLTF': 'GLB' if props.gltf_format == 'GLB' else 'glTF',
                'OBJ': 'OBJ',
            }
            subfolder = format_folders.get(props.export_format, 'Exports')
            box.label(text=f"Output: {blend_name}-export/{subfolder}/", icon='INFO')
