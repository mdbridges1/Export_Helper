# Export Helper Pro

A Blender add-on for batch exporting objects and collections to FBX, glTF, and OBJ formats with engine-specific presets for Unity, Unreal, and Godot.

**Version:** 2.0.0
**Blender:** 4.2+ / 5.0 compatible
**Location:** View3D > Sidebar (N) > Export tab

## Features

### Export Formats
- **FBX (Unity)** - Optimised settings for Unity import
- **FBX (Unreal)** - Optimised settings for Unreal Engine
- **FBX (Generic)** - Standard FBX settings for other applications
- **glTF/GLB** - glTF 2.0 for Godot, web, and modern engines
- **OBJ** - Wavefront OBJ with PBR material extensions

### Export Modes
- **Export All Objects** - Export every mesh in the scene as individual files
- **Export Selected** - Export only selected objects individually
- **Quick Collection Export** - Export a single collection (with sub-collections) as one file
- **Multi-Collection Export** - Batch export multiple collections, each as its own file

### Smart Features
- **Viewport Colour Conversion** - Automatically converts Viewport Display colours to Principled BSDF materials during export, ensuring colours appear in your target engine
- **Sharp Edge Preservation** - Temporarily applies Edge Split modifier to preserve flat shading on marked sharp edges (glTF/OBJ)
- **Centre Origins** - Optionally moves objects to world origin during export, then restores them
- **Recursive Collections** - Collection exports include all objects from nested sub-collections
- **Armature Inclusion** - Automatically includes armatures when exporting rigged meshes (FBX)
- **Embed Textures** - Option to embed textures inside FBX files for portability

## Installation

1. Download the `.zip` file from the releases
2. In Blender: **Edit > Preferences > Add-ons > Install**
3. Navigate to and select the downloaded `.zip` file
4. Enable "Export Helper Pro" in the add-ons list

## Usage

### Basic Setup
1. **Save your .blend file** - The add-on creates export folders relative to your file location
2. Open the sidebar in the 3D View (press **N**)
3. Select the **Export** tab

### Export Options

| Option | Description |
|--------|-------------|
| **Centre Origins** | Temporarily moves objects to world origin for export, then restores their position |
| **Convert Viewport Colours** | Creates Principled BSDF materials from Viewport Display colours |
| **Include Armatures** | Includes armatures when exporting rigged meshes (FBX only) |
| **Embed Textures** | Embeds textures inside FBX files (FBX only) |
| **Preserve Sharp Edges** | Applies temporary Edge Split modifier for flat shading (glTF/OBJ) |
| **glTF Format** | Choose between GLB (single binary) or glTF + separate files |

### Export Workflows

#### Individual Objects
1. Select your export format
2. Click **Export All Objects** to export every mesh, or
3. Select specific objects and click **Export Selected**

#### Single Collection
1. In the "Quick Collection Export" section, select your target collection
2. The panel shows object count and sub-collection info
3. Click **Export Collection** - all objects (including nested sub-collections) export as one file

#### Multiple Collections
1. In the "Multi-Collection Export" section, click **+** to add collections
2. Or click the preset icon to add all scene collections automatically
3. Toggle checkboxes to enable/disable individual collections
4. Click **Export X Collections** to batch export

### Open Export Folder
Click **Open Export Folder** to open the output directory in your file browser.

## Output Structure

Exports are organised in a folder next to your .blend file:

```
yourfile.blend
yourfile-export/
├── FBX_Unity/      # Unity FBX exports
├── FBX_Unreal/     # Unreal FBX exports
├── FBX/            # Generic FBX exports
├── GLB/            # glTF binary exports
├── glTF/           # glTF separate exports
└── OBJ/            # OBJ exports
```

Each object or collection is exported with its Blender name as the filename.

## Format-Specific Settings

### FBX (Unity)
- Face-based smoothing
- Tangent space enabled
- No leaf bones (cleaner skeleton hierarchy)
- Y-up, -Z forward axis

### FBX (Unreal)
- Edge-based smoothing
- Mesh edges preserved
- Tangent space enabled
- No leaf bones
- Y-up, -Z forward axis

### FBX (Generic)
- Face-based smoothing
- Baked transforms
- Standard settings for general use

### glTF/GLB
- Applied modifiers
- Tangents and normals exported
- Y-up orientation
- GLB: Single binary file with embedded textures
- glTF: Separate .gltf, .bin, and texture files

### OBJ
- PBR material extensions enabled
- Applied modifiers
- UVs and normals exported
- Y-up, -Z forward axis

## Viewport Colour Workflow

This feature is particularly useful for game asset workflows where you:

1. Model objects using simple Viewport Display colours (no shader nodes)
2. Want those colours to appear in your game engine

**How it works:**
- Materials without Principled BSDF nodes are temporarily converted during export
- The Viewport Display colour becomes the Base Colour
- Original materials are restored after export

## Sharp Edge Workflow

For hard-surface models with flat shading:

1. In Edit Mode, select edges you want sharp
2. **Edge > Mark Sharp**
3. Enable "Preserve Sharp Edges" in the export panel
4. Export to glTF or OBJ

The add-on temporarily adds an Edge Split modifier (using marked sharp edges only), exports, then removes it.

## Compatibility

- **Blender 4.2+** - Fully supported
- **Blender 5.0** - Fully supported
- **Older versions** - May work but untested; some features require 4.x APIs

## Credits

- **Michael Bridges** - Original Export Helper add-on
- **Embark Studios** - Inspiration from blender-tools

## Licence

MIT Licence

---

For issues or feature requests, visit: https://github.com/mdbridges1/Export_Helper
