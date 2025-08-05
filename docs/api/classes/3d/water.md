=== "Constructors"

    | Function | Description |
    | - | - |
    | Water.new() | Creates a blank water object |
    | Water.new([Vector2D][vector2d] `tileSize`, [Vector2D][vector2d] `tileCount`, [Vector2D][vector2d] `textureRepeat`) | Creates water with grid dimensions and texture scaling |
    | Water.new([Material][material] `material`) | Creates water using the given material |
    | Water.new(table `t`) | Creates water from a table of values: { height = float, speed = float, length = float, tileSize = Vector2D, tileCount = Vector2D, textureRepeat = Vector2D, material = Material } |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector3D][vector3d] | Water position |
    | .rotation | [Vector3D][vector3d] | Water rotation |
    | .scale | [Vector3D][vector3d] | Water scale |
    | .visible | bool | Whether water is visible |
    | .height | float | Height of waves |
    | .speed | float | Speed of waves |
    | .length | float | Length of waves |
    | .shadows | int | Enable shadows (legacy only); see [SHADOW_MODE][shadow_mode] |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :destroy() |  | Destroys the water object |
    | :loadMaterial([Material][material] `material`) |  | Loads the given material |
    | :ignoreLighting() |  | Disables lighting for this object |
    | :setParent(3DObject `other`) |  | Parents this water object to another 3D object |
    | :getAbsolutePosition() | [Vector3D][vector3d] | Returns world-space position |
    | :getAbsoluteRotation() | [Vector3D][vector3d] | Returns world-space rotation |
    | :getAbsoluteScale() | [Vector3D][vector3d] | Returns world-space scale |
    | :updateAbsolutePosition() |  | Updates world transform (non-recursive) |

[shadow_mode]: https://darttheg.github.io/LimeAPI/api/structs.html#shadow_mode

[vector2d]: https://darttheg.github.io/LimeAPI/api/classes/vector2d.html
[vector3d]: https://darttheg.github.io/LimeAPI/api/classes/vector3d.html
[vector4d]: https://darttheg.github.io/LimeAPI/api/classes/vector4d.html
[material]: https://darttheg.github.io/LimeAPI/api/classes/3d/material.html