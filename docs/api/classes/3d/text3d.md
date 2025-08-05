=== "Constructors"

    | Function | Description |
    | - | - |
    | Text3D.new() | Creates an empty 3D text object |
    | Text3D.new(String `text`) | Creates a 3D text object with the given `text` |
    | Text3D.new(String `text`, String `fontName`) | Creates a 3D text object with specified `text` and `fontName` |
    | Text3D.new(String `text`, [Vector3D][vector3d] `position`) | Creates a 3D text object with `text` at `position` |
    | Text3D.new(String `text`, [Vector3D][vector3d] `position`, [Vector4D][vector4d] `color`) | Creates a 3D text object with `text`, `position`, and `color` |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .text | String | The displayed text |
    | .position | [Vector3D][vector3d] | Position of the text |
    | .visible | bool | Whether the text is visible |
    | .textColor | [Vector4D][vector4d] | Text color |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :destroy() |  | Destroys the object |
    | :setParent(3DObject `other`) |  | Parents this object to another 3D object |
    | :getAbsolutePosition() | [Vector3D][vector3d] | Returns world-space position |
    | :getAbsoluteRotation() | [Vector3D][vector3d] | Returns world-space rotation |
    | :getAbsoluteScale() | [Vector3D][vector3d] | Returns world-space scale |
    | :updateAbsolutePosition() |  | Updates world transform (non-recursive) |

[vector2d]: https://darttheg.github.io/LimeAPI/api/classes/vector2d.html
[vector3d]: https://darttheg.github.io/LimeAPI/api/classes/vector3d.html
[vector4d]: https://darttheg.github.io/LimeAPI/api/classes/vector4d.html
[texture]: https://darttheg.github.io/LimeAPI/api/classes/texture.html