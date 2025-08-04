=== "Constructors"

    | Function | Description |
    | - | - |
    | Water.new() | Creates a blank water object |
    | Water.new([Vector2D](vector2d.md) `tileSize`, [Vector2D](vector2d.md) `tileCount`, [Vector2D](vector2d.md) `textureRepeat`) | Creates water with grid dimensions and texture scaling |
    | Water.new([Material](material.md) `material`) | Creates water using the given material |
    | Water.new(table `t`) | Creates water from a table of values: { height = float, speed = float, length = float, tileSize = Vector2D, tileCount = Vector2D, textureRepeat = Vector2D, material = Material } |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector3D](vector3d.md) | Water position |
    | .rotation | [Vector3D](vector3d.md) | Water rotation |
    | .scale | [Vector3D](vector3d.md) | Water scale |
    | .visible | bool | Whether water is visible |
    | .height | float | Height of waves |
    | .speed | float | Speed of waves |
    | .length | float | Length of waves |
    | .shadows | int | Enable shadows (legacy only); see `irrlicht.SHADOW_MODE` |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :destroy() |  | Destroys the water object |
    | :loadMaterial([Material](material.md) `material`) |  | Loads the given material |
    | :ignoreLighting() |  | Disables lighting for this object |
    | :setParent(3DObject `other`) |  | Parents this water object to another 3D object |
    | :getAbsolutePosition() | [Vector3D](vector3d.md) | Returns world-space position |
    | :getAbsoluteRotation() | [Vector3D](vector3d.md) | Returns world-space rotation |
    | :getAbsoluteScale() | [Vector3D](vector3d.md) | Returns world-space scale |
    | :updateAbsolutePosition() |  | Updates world transform (non-recursive) |