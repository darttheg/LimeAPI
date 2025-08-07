=== "Constructors"

    | Function | Description |
    | - | - |
    | Empty.new() | Creates an empty object |
    | Empty.new([Vector3D][vector3d] `position`) | Creates an empty object at `position` |
    | Empty.new([Vector3D][vector3d] `position`, [Vector3D][vector3d] `rotation`) | Creates an empty object at `position` with `rotation` |
    | Empty.new([Vector3D][vector3d] `position`, [Vector3D][vector3d] `rotation`, [Vector3D][vector3d] `scale`) | Creates an empty object with full transform |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector3D][vector3d] | Object position |
    | .rotation | [Vector3D][vector3d] | Object rotation |
    | .scale | [Vector3D][vector3d] | Object scale |
    | .visible | bool | Object visibility |
    | .debug | bool | Enable/disable debug visualization |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :destroy() |  | Destroys the object |
    | :setParent(3DObject `other`) |  | Parents this object to another 3D object |
    | :getBoundingBox() | Lua table | Returns bounding box info: { min = Vector3D, max = Vector3D } |
    | :getAbsolutePosition() | [Vector3D][vector3d] | Returns world-space position |
    | :getAbsoluteRotation() | [Vector3D][vector3d] | Returns world-space rotation |
    | :getAbsoluteScale() | [Vector3D][vector3d] | Returns world-space scale |
    | :updateAbsolutePosition() |  | Updates world transform (non-recursive) |

[vector2d]: https://darttheg.github.io/LimeAPI/api/classes/vector2d.html
[vector3d]: https://darttheg.github.io/LimeAPI/api/classes/vector3d.html
[vector4d]: https://darttheg.github.io/LimeAPI/api/classes/vector4d.html
[texture]: https://darttheg.github.io/LimeAPI/api/classes/texture.html