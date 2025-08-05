=== "Constructors"

    | Function | Description |
    | - | - |
    | Billboard.new() | Creates an empty billboard |
    | Billboard.new(Billboard `other`) | Creates a copy of another billboard |
    | Billboard.new([Material][material] `material`) | Creates a billboard using the given material |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector3D][vector3d] | Billboard position |
    | .size | [Vector2D][vector2d] | Billboard size |
    | .yPivot | float | Vertical pivot point of the billboard |
    | .lockAxis | [Vector3D][vector3d] | Lock axis from rotating (each axis uses a bool value) |
    | .visible | bool | Billboard visibility |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :loadMaterial([Material][material] `material`) |  | Loads a material into the billboard |
    | :destroy() |  | Destroys the billboard |
    | :setParent(3DObject `other`) |  | Parents this billboard to another 3D object |
    | :getAbsolutePosition() | [Vector3D][vector3d] | Returns world-space position |
    | :getAbsoluteRotation() | [Vector3D][vector3d] | Returns world-space rotation |
    | :getAbsoluteScale() | [Vector3D][vector3d] | Returns world-space scale |
    | :updateAbsolutePosition() |  | Updates world transform (non-recursive) |

[vector2d]: https://darttheg.github.io/LimeAPI/api/classes/vector2d.html
[vector3d]: https://darttheg.github.io/LimeAPI/api/classes/vector3d.html
[vector4d]: https://darttheg.github.io/LimeAPI/api/classes/vector4d.html
[material]: https://darttheg.github.io/LimeAPI/api/classes/3d/material.html