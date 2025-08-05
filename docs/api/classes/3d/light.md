> **Note:** This class is incompatible with Legacy Drawing.

=== "Constructors"

    | Function | Description |
    | - | - |
    | Light.new() | Creates a default light |
    | Light.new([Vector3D][vector3d] `position`, [Vector3D][vector3d] `rotation`, [Vector4D][vector4d] `color`) | Creates a light at `position` with `rotation` and `color` |
    | Light.new([Vector3D][vector3d] `position`, [Vector3D][vector3d] `rotation`, [Vector4D][vector4d] `color`, [Vector2D][vector2d] `shadowPrecision`, float `fieldOfView`, bool `directional`) | Creates a light with full configuration including shadow precision and directionality |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector3D][vector3d] | Light position |
    | .rotation | [Vector3D][vector3d] | Light rotation |
    | .color | [Vector4D][vector4d] | Light color |
    | .debug | bool | Show debug data |
    | .precisionPlanes | [Vector2D][vector2d] | Shadow depth precision — closer values yield better results |
    | .fieldOfView | float | Field of view angle (affects light projection) |
    | .directional | bool | Whether the light is directional |
    | .active | bool | Whether the light is active in rendering |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :destroy() |  | Destroys the object |
    | :setParent(3DObject `other`) |  | Parents this light to another 3D object |
    | :getAbsolutePosition() | [Vector3D][vector3d] | Returns world position |
    | :getAbsoluteRotation() | [Vector3D][vector3d] | Returns world rotation |
    | :getAbsoluteScale() | [Vector3D][vector3d] | Returns world scale |
    | :updateAbsolutePosition() |  | Updates world transform (non-recursive) |

[vector2d]: https://darttheg.github.io/LimeAPI/api/classes/vector2d.html
[vector3d]: https://darttheg.github.io/LimeAPI/api/classes/vector3d.html
[vector4d]: https://darttheg.github.io/LimeAPI/api/classes/vector4d.html
[texture]: https://darttheg.github.io/LimeAPI/api/classes/texture.html