> **Note:** This class is incompatible with Legacy Drawing.

=== "Constructors"

    | Function | Description |
    | - | - |
    | Light.new() | Creates a default light |
    | Light.new([Vector3D](vector3d.md) `position`, [Vector3D](vector3d.md) `rotation`, [Vector4D](vector4d.md) `color`) | Creates a light at `position` with `rotation` and `color` |
    | Light.new([Vector3D](vector3d.md) `position`, [Vector3D](vector3d.md) `rotation`, [Vector4D](vector4d.md) `color`, [Vector2D](vector2d.md) `shadowPrecision`, float `fieldOfView`, bool `directional`) | Creates a light with full configuration including shadow precision and directionality |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector3D](vector3d.md) | Light position |
    | .rotation | [Vector3D](vector3d.md) | Light rotation |
    | .color | [Vector4D](vector4d.md) | Light color |
    | .debug | bool | Show debug data |
    | .precisionPlanes | [Vector2D](vector2d.md) | Shadow depth precision — closer values yield better results |
    | .fieldOfView | float | Field of view angle (affects light projection) |
    | .directional | bool | Whether the light is directional |
    | .active | bool | Whether the light is active in rendering |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :destroy() |  | Destroys the object |
    | :setParent(3DObject `other`) |  | Parents this light to another 3D object |
    | :getAbsolutePosition() | [Vector3D](vector3d.md) | Returns world position |
    | :getAbsoluteRotation() | [Vector3D](vector3d.md) | Returns world rotation |
    | :getAbsoluteScale() | [Vector3D](vector3d.md) | Returns world scale |
    | :updateAbsolutePosition() |  | Updates world transform (non-recursive) |