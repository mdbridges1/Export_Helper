# Export Helper

This add-on is designed to quickly export every object in your blend file to one of 4 formats:
+ GLB (glTF 2.0 binary)
+ OBJ
+ FBX
+ FBX for Unity

It is currently designed to take each object, and centre it in the scene and export, then places the model back. where it was in the scene.

### Limitations
+ Currently doesn't work well with multi-object models with uncommon origins.
+ Not tested with animations at the moment.

I developed it as part of creating a series of modular game assets and quickly realised it would be quicker to write a little script to export it than do the work manually.  It has grown since then, becoming an add-on with multiple export options.

If you have any feedback, either on its functionality or codebase please let me know :D

and if you want to see additional functionality or have a request for a different type of add on let me know as well.

Mikey

## Installation
1. Download .zip file
1. Open Blender
1. Edit>Preferences Select the add-on tab
1. Click Install
1. Navigate to your download folder and select Export_Helper_1.0.zip
1. Put a tick in the Export_Helper add on to enable it.

## Using The Export Helper

I recommend that you create a new scene containing specifically for what you want to export from your blend file.

1. With the 3D viewport open up the side bar ( N Key )
1. Click oin the "Export Helper" Tab
1. Select which file type you wna to export
1. In the same folder your .blend file is a new folder will be created with all of the objects in the scene exported and ready for use externally.

**WARNINGS**
+ *There is no checking for existing files, any thing with the same name will be overwritten.*

+ *Unity Export - The export process will current apply scale and rotation transforms and will make Object_Data unique for all meshes in the scene*


## Attribution 4.0 International (CC BY 4.0)
This is a human-readable summary of (and not a substitute for) the license.
## You are free to:
Share — copy and redistribute the material in any medium or format
Adapt — remix, transform, and build upon the material
for any purpose, even commercially.

## Under the following terms:
Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

## Resources I found really useful:

### Blender Manual

https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html#
https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html#your-first-add-on

### Reading List and Questions:
https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API/Addons
https://wiki.blender.org/wiki/Reference/Release_Notes/2.80/Python_API
https://docs.blender.org/api/current/bpy.utils.html
https://devtalk.blender.org/t/add-on-panel-missing-from-active-tool-workspace-settings/7349
https://blender.stackexchange.com/questions/106203/scripting-error-using-view3d/106319
https://blender.stackexchange.com/questions/81388/center-cursor-in-python-script
https://blender.stackexchange.com/questions/5784/why-does-operators-bl-idname-have-to-contain-1-dot

https://blender.stackexchange.com/questions/57306/how-to-create-a-custom-ui
https://blender.stackexchange.com/questions/8699/what-ui-would-work-for-choosing-from-a-long-long-list
https://blender.stackexchange.com/questions/132825/python-selecting-object-by-name-in-2-8
https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/#Looping_in_Python
https://automatetheboringstuff.com/chapter8/
https://blender.stackexchange.com/questions/7085/error-in-addon-wm-operator-invoke-invalid-operator-call
https://blender.stackexchange.com/questions/2545/quick-way-to-get-current-opened-filename-in-a-script

### YouTube:

https://www.youtube.com/watch?v=uahfuypQQ04

