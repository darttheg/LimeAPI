=== "Constructors"

    | Function | Description |
    | - | - |
    | Hitbox.new() | Creates an empty capsule-shaped hitbox |
    | Hitbox.new(float `radius`, float `height`) | Creates a capsule hitbox with given radius and height |
    | Hitbox.new(Hitbox `other`) | Creates a copy of another hitbox |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector3D](vector3d.md) | Hitbox position |
    | .rotation | [Vector3D](vector3d.md) | Hitbox rotation |
    | .active | bool | Whether the hitbox is active for overlap detection and ray collision |
    | .debug | bool | Show debug visuals; yellow = active, blue = inactive |
    | .levelOfDetail | int | Debug visual quality (`0` = low, `1` = medium, `2` = high) — may be bugged |
    | .collision | bool | Enable raypick collision |
    | .ID | int | Hitbox ID |
    | .radius | float | Capsule radius |
    | .height | float | Capsule height |
    | .attributes | [Vector2D](vector2d.md) | Radius and height packed into a Vector2D |