=== "Constructors"

    | Function | Description |
    | - | - |
    | Trail.new() | Creates a new trail object |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector3D](vector3d.md) | Trail position |
    | .rotation | [Vector3D](vector3d.md) | Trail rotation |
    | .scale | [Vector3D](vector3d.md) | Trail scale |
    | .visible | bool | Set/get visibility of the trail |
    | .debug | bool | Enable/disable debug data |
    | .shadows | int | Enable shadows (legacy only); see `irrlicht.SHADOW_MODE` |
    | .height | float | Set/get trail height |
    | .wind | [Vector3D](vector3d.md) | Wind velocity |
    | .segments | int | Number of segments in trail |
    | .alignment | int | Trail axis alignment; see `irrlicht.TRAIL_ALIGNMENT_TYPE` |
    | .segmentLength | float | Fixed segment length; set to `0` to use dynamic length |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :destroy() |  | Removes the trail in Irrlicht |
    | :ignoreLighting() |  | Excludes trail from lighting calculations permanently |
    | :loadMaterial([Material](material.md) `material`) |  | Loads the material |
    | :updateNormals(bool `enable`) |  | If enabled, will update normals as well as vertex positions (may have no effect) |
    | :setParent(3DObject `other`) |  | Parents this 3D object to another |
    | :getAbsolutePosition() | [Vector3D](vector3d.md) | Returns world position |
    | :getAbsoluteRotation() | [Vector3D](vector3d.md) | Returns world rotation |
    | :getAbsoluteScale() | [Vector3D](vector3d.md) | Returns world scale |
    | :updateAbsolutePosition() |  | Updates world transform (non-recursive) |