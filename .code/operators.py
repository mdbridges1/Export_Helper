# SPDX-License-Identifier: MIT
# Export Helper Pro - Operator classes

import os
import subprocess
import sys

import bpy
from bpy.types import Operator
from .utils import (
    get_export_path,
    get_exportable_objects,
    get_collection_objects_recursive,
    count_subcollections_recursive,
)
from .exporters import (
    do_export_objects,
    do_export_collection,
)


class EXPORT_HELPER_OT_export_all(Operator):
    """Export all mesh objects in the scene individually"""
    bl_idname = "export_helper.export_all"
    bl_label = "Export All Objects"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        export_dir = get_export_path(context)
        if not export_dir:
            self.report({'ERROR'}, "Save your .blend file first!")
            return {'CANCELLED'}

        props = context.scene.export_helper_props
        all_objects = list(context.scene.objects)

        success, fail = do_export_objects(context, all_objects, export_dir, props)

        if fail > 0:
            self.report({'WARNING'}, f"Exported {success} objects, {fail} failed")
        else:
            self.report({'INFO'}, f"Exported {success} objects to {export_dir}")

        return {'FINISHED'}


class EXPORT_HELPER_OT_export_selected(Operator):
    """Export selected objects individually"""
    bl_idname = "export_helper.export_selected"
    bl_label = "Export Selected"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        export_dir = get_export_path(context)
        if not export_dir:
            self.report({'ERROR'}, "Save your .blend file first!")
            return {'CANCELLED'}

        if not context.selected_objects:
            self.report({'ERROR'}, "No objects selected!")
            return {'CANCELLED'}

        props = context.scene.export_helper_props
        selected_objects = list(context.selected_objects)

        success, fail = do_export_objects(context, selected_objects, export_dir, props)

        if fail > 0:
            self.report({'WARNING'}, f"Exported {success} objects, {fail} failed")
        else:
            self.report({'INFO'}, f"Exported {success} objects to {export_dir}")

        return {'FINISHED'}


class EXPORT_HELPER_OT_export_collection(Operator):
    """Export the target collection (including sub-collections) as a single file"""
    bl_idname = "export_helper.export_collection"
    bl_label = "Export Collection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        export_dir = get_export_path(context)
        if not export_dir:
            self.report({'ERROR'}, "Save your .blend file first!")
            return {'CANCELLED'}

        props = context.scene.export_helper_props
        collection = props.target_collection

        if not collection:
            self.report({'ERROR'}, "No collection selected!")
            return {'CANCELLED'}

        success, error = do_export_collection(context, collection, export_dir, props)

        if success:
            obj_count = len(get_exportable_objects(context, get_collection_objects_recursive(collection)))
            subcol_count = count_subcollections_recursive(collection)
            if subcol_count > 0:
                self.report({'INFO'}, f"Exported '{collection.name}' ({obj_count} objects from {subcol_count + 1} collections)")
            else:
                self.report({'INFO'}, f"Exported '{collection.name}' ({obj_count} objects)")
        else:
            self.report({'ERROR'}, f"Export failed: {error}")
            return {'CANCELLED'}

        return {'FINISHED'}


class EXPORT_HELPER_OT_add_collection(Operator):
    """Add a collection to the export list"""
    bl_idname = "export_helper.add_collection"
    bl_label = "Add Collection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.export_helper_props
        props.export_collections.add()
        props.active_collection_index = len(props.export_collections) - 1
        return {'FINISHED'}


class EXPORT_HELPER_OT_remove_collection(Operator):
    """Remove selected collection from the export list"""
    bl_idname = "export_helper.remove_collection"
    bl_label = "Remove Collection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.export_helper_props
        index = props.active_collection_index

        if 0 <= index < len(props.export_collections):
            props.export_collections.remove(index)
            props.active_collection_index = min(index, len(props.export_collections) - 1)

        return {'FINISHED'}


class EXPORT_HELPER_OT_add_all_collections(Operator):
    """Add all scene collections to the export list"""
    bl_idname = "export_helper.add_all_collections"
    bl_label = "Add All Collections"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        props = context.scene.export_helper_props
        props.export_collections.clear()

        def add_collections_recursive(collection, depth=0):
            if collection.name != "Scene Collection" or depth > 0:
                all_objs = get_collection_objects_recursive(collection)
                if get_exportable_objects(context, all_objs):
                    item = props.export_collections.add()
                    item.collection = collection
                    item.export_enabled = True

        for col in context.scene.collection.children:
            add_collections_recursive(col)

        self.report({'INFO'}, f"Added {len(props.export_collections)} collections")
        return {'FINISHED'}


class EXPORT_HELPER_OT_export_multi_collections(Operator):
    """Export all enabled collections in the list"""
    bl_idname = "export_helper.export_multi_collections"
    bl_label = "Export All Listed Collections"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        export_dir = get_export_path(context)
        if not export_dir:
            self.report({'ERROR'}, "Save your .blend file first!")
            return {'CANCELLED'}

        props = context.scene.export_helper_props

        to_export = [item for item in props.export_collections
                     if item.export_enabled and item.collection]

        if not to_export:
            self.report({'ERROR'}, "No collections enabled for export!")
            return {'CANCELLED'}

        success_count = 0
        fail_count = 0

        for item in to_export:
            success, error = do_export_collection(context, item.collection, export_dir, props)
            if success:
                success_count += 1
            else:
                fail_count += 1
                print(f"Failed to export '{item.collection.name}': {error}")

        if fail_count > 0:
            self.report({'WARNING'}, f"Exported {success_count} collections, {fail_count} failed")
        else:
            self.report({'INFO'}, f"Exported {success_count} collections to {export_dir}")

        return {'FINISHED'}


class EXPORT_HELPER_OT_open_export_folder(Operator):
    """Open the export folder in file browser"""
    bl_idname = "export_helper.open_folder"
    bl_label = "Open Export Folder"
    bl_options = {'REGISTER'}

    def execute(self, context):
        export_dir = get_export_path(context)
        if not export_dir:
            self.report({'ERROR'}, "Save your .blend file first!")
            return {'CANCELLED'}

        if sys.platform == 'win32':
            os.startfile(str(export_dir))
        elif sys.platform == 'darwin':
            subprocess.Popen(['open', str(export_dir)])
        else:
            subprocess.Popen(['xdg-open', str(export_dir)])

        return {'FINISHED'}
