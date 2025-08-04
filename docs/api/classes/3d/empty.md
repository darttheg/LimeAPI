=== "Constructors"

    | Function | Description |
    | - | - |
    | Empty.new() | Creates an empty object |
    | Empty.new([Vector3D](vector3d.md) `position`) | Creates an empty object at `position` |
    | Empty.new([Vector3D](vector3d.md) `position`, [Vector3D](vector3d.md) `rotation`) | Creates an empty object at `position` with `rotation` |
    | Empty.new([Vector3D](vector3d.md) `position`, [Vector3D](vector3d.md) `rotation`, [Vector3D](vector3d.md) `scale`) | Creates an empty object with full transform |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector3D](vector3d.md) | Object position |
    | .rotation | [Vector3D](vector3d.md) | Object rotation |
    | .scale | [Vector3D](vector3d.md) | Object scale |
    | .visible | bool | Object visibility |
    | .debug | bool | Enable/disable debug visualization |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :destroy() |  | Destroys the object |
    | :setParent(3DObject `other`) |  | Parents this object to another 3D object |
    | :getBoundingBox() | Lua table | Returns bounding box info: { min = Vector3D, max = Vector3D } |
    | :getAbsolutePosition() | [Vector3D](vector3d.md) | Returns world-space position |
    | :getAbsoluteRotation() | [Vector3D](vector3d.md) | Returns world-space rotation |
    | :getAbsoluteScale() | [Vector3D](vector3d.md) | Returns world-space scale |
    | :updateAbsolutePosition() |  | Updates world transform (non-recursive) |