=== "Constructors"

    | Function | Description |
    | - | - |
    | Billboard.new() | Creates an empty billboard |
    | Billboard.new(Billboard `other`) | Creates a copy of another billboard |
    | Billboard.new([Material](material.md) `material`) | Creates a billboard using the given material |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector3D](vector3d.md) | Billboard position |
    | .size | [Vector2D](vector2d.md) | Billboard size |
    | .yPivot | float | Vertical pivot point of the billboard |
    | .lockAxis | [Vector3D](vector3d.md) | Lock axis from rotating (each axis uses a bool value) |
    | .visible | bool | Billboard visibility |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :loadMaterial([Material](material.md) `material`) |  | Loads a material into the billboard |
    | :destroy() |  | Destroys the billboard |
    | :setParent(3DObject `other`) |  | Parents this billboard to another 3D object |
    | :getAbsolutePosition() | [Vector3D](vector3d.md) | Returns world-space position |
    | :getAbsoluteRotation() | [Vector3D](vector3d.md) | Returns world-space rotation |
    | :getAbsoluteScale() | [Vector3D](vector3d.md) | Returns world-space scale |
    | :updateAbsolutePosition() |  | Updates world transform (non-recursive) |