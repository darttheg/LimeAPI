=== "Constructors"

    | Function | Description |
    | - | - |
    | Mesh.new() | Creates an empty mesh |
    | Mesh.new(String `meshPath`) | Loads a mesh from `path` |
    | Mesh.new(Mesh `other`) | Creates a copy of another mesh |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector3D](vector3d.md) | Mesh position |
    | .rotation | [Vector3D](vector3d.md) | Mesh rotation |
    | .scale | [Vector3D](vector3d.md) | Mesh scale |
    | .visible | bool | Mesh visibility |
    | .ID | int | Mesh ID (defaults to -1; intended to change to positive int for optimization) |
    | .collision | bool | Enable/disable collision |
    | .frame | int | Frame of animation |
    | .debug | bool | Enable/disable debug data |
    | .vertexColor | [Vector4D](vector4d.md) | Vertex color; use `EMT_TRANSPARENT_VERTEX_ALPHA` to apply alpha blending |
    | .shadows | int | Enable shadows (legacy only); see `irrlicht.SHADOW_MODE` |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :load(String `path`) |  | Loads a mesh from `path` |
    | :loadFromBuffer([MeshBuffer](meshbuffer.md) `buffer`) |  | Loads mesh data from a mesh buffer |
    | :loadMaterial([Material](material.md) `material`, int `slot`) |  | Loads `material` into `slot` index |
    | :destroy() |  | Destroys the object |
    | :writeToFile(String `path`) |  | Exports mesh in COLLADA format to `path` |
    | :getVertexCount() | int | Returns the number of vertices in the mesh |
    | :getMaterialCount() | int | Returns the number of material slots |
    | :toStr() | String | Returns the mesh path as a String |
    | :getBoneDataByName(String `name`) | Lua table | Returns bone data for the bone with the given name:<br> <br>```lua\n{\n  name = String,\n  rotation = Vector3D,\n  headPosition = Vector3D,\n  tailPosition = Vector3D,\n  length = float\n}``` |
    | :getBoneDataByIndex(int `index`) | Lua table | Identical to `:getBoneDataByName` but uses an index |
    | :getBoundingBox() | Lua table | Returns bounding box data:<br><br>```lua\n{\n  min = Vector3D,\n  max = Vector3D\n}``` |
    | :getFrameCount() | int | Returns number of animation frames |
    | :normalizeNormals(bool `enable`) |  | Enables/disables normal normalization |
    | :toPlanarMapping() |  | Applies planar UV mapping to the mesh |
    | :setHardwareMappingHint(int `hint`) |  | Sets hardware mapping strategy. See `irrlicht.HARDWARE_MAPPING_HINT`:<br><br>• `Never` – Do not store on hardware<br>• `Static` – Rarely changed<br>• `Dynamic` – Frequently changed<br>• `Stream` – Always changed |
    | :ignoreLighting() |  | Excludes this mesh from lighting calculations (not applicable in legacy rendering) |
    | :setParent(3DObject `other`) |  | Parents this mesh to another 3D object |
    | :getAbsolutePosition() | [Vector3D](vector3d.md) | Returns world position |
    | :getAbsoluteRotation() | [Vector3D](vector3d.md) | Returns world rotation |
    | :getAbsoluteScale() | [Vector3D](vector3d.md) | Returns world scale |
    | :updateAbsolutePosition() |  | Updates world transform (non-recursive) |
    | :setAutomaticCulling(bool `enable`) |  | Enables/disables auto-culling based on bounding box |