# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Export Helper",
    "author" : "Michael Bridges",
    "description" : "Will automatically export all objects in a scene to .glb, fbx and obj format. These files will export into their own subfolders with tthe .blend file. \n Know Issues: \nNo check whether the .blend file is saved, if it isnt export will fail.\nNo consideration for other .blend file in the same folder is taken.  Duplicate objectnames will overwrite existing data.",
    "blender" : (2, 80, 0),
    "version" : (0, 9, 1),
    "location" : "View 3D > Sidebar > Export Helper",
    "warning" : "",
    "category" : "Export"
} 

import bpy

from . test_op import EXPORT_OT_Operator
from . test_panel import EXPORT_PT_Panel

classes = (EXPORT_OT_Operator, EXPORT_PT_Panel)

register, unregister = bpy.utils.register_classes_factory(classes)