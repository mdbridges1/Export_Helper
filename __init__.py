bl_info = {
    "name" : "Export Helper",
    "author" : "Michael Bridges",
    "description" : "Will automatically export all objects in a scene to .glb, fbx and obj format. \nThese files will export into their own subfolders with the .blend file. \n Know Issues: \nNo check whether the .blend file is saved, if it isnt export will fail.\nNo consideration for other .blend file in the same folder is taken.  Duplicate objectnames will overwrite existing data.",
    "blender" : (2, 80, 0),
    "version" : (0, 9, 2),
    "location" : "View 3D > Sidebar > Export Helper",
    "warning" : "",
    "category" : "Export"
} 

import bpy

from . test_op import EXPORT_OT_Operator
from . test_panel import EXPORT_PT_Panel

classes = (EXPORT_OT_Operator, EXPORT_PT_Panel)

register, unregister = bpy.utils.register_classes_factory(classes)