# Patch Notes

## v1.2  
+ Added in the abilty to Export all objects in a scene as one file. (GLB only at the moment)
+ Tweaked UI to be distinct Sections

## Potential Issues:
+ Currently doesn't work well with multi-object models with uncommon origins.
+ Not tested with animations at the moment.

## Release v1.1
+ My First Hotfix? -Yay  :D
+ Fixed bug in OBJ export, where Object wouldn't go back to there original location.
+ Fixed versioning issue on v1.0 release.

## Release v1.0
+ Release Ready.
+ Fixed having to be in object mode for the add on to function.
+ Ready to wider scrunity.

## v0.94
+ Dedicated buttons added for each export type

  + GLB
  + OBJ
  + FBX
  + FBX for Unity

## v0.93
+ Dedicated FBX Unity files now exported automagically.
+ Adjusted FBX eport settings to remove smoothing group warnings when importing into Unreal.
+ Tested in:

  + Godot 3.2
  + Unity 2019.3.13f1
  + Unreal 4.25

## v0.92 
Added code to locate objects to world origin, Export, and put back to original location. 

## v0.91 
Code working and complete

### Fixed Issues:
+ ~~Rotation issue with FBX Export in Unity - didicated Unity FBX export might be necessary~~
+ ~~User gets 4 folders with 4 file types -add option to only export the types needed.~~
+ ~~Script fails if user isn't in Object Mode~~