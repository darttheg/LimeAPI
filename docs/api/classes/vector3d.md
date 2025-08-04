=== "Constructors"

    | Function | Description |
    | - | - |
    | Vector3D.new() | Creates a default Vector3D (0, 0, 0) |
    | Vector3D.new(float `x`, float `y`, float `z`) | Creates a Vector3D with `x`, `y`, and `z` components |
    | Vector3D.new(float `x`) | Creates a Vector3D with all components set to `x` |

=== "Operations"

    | Operator | Description |
    | - | - |
    | `==` | Checks equality between two Vector3D objects |
    | `+` | Adds two Vector3D objects |
    | `-` | Subtracts one Vector3D from another |
    | `*` | Multiplies a Vector3D by a scalar |
    | `/` | Divides a Vector3D by a scalar |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :length() | float | Returns the length (magnitude) of the Vector3D |
    | :normalize() | [Vector3D](vector3d.md) | Returns a normalized Vector3D in range [0, 1] |
    | :normalizeToRange(float `x`, float `y`) | [Vector3D](vector3d.md) | Returns a Vector3D normalized to the range [`x`, `y`] |
    | :dot([Vector3D](vector3d.md) `x`) | float | Returns the dot product with vector `x` |
    | :rotate([Vector3D](vector3d.md) `x`) | [Vector3D](vector3d.md) | Returns the vector rotated by vector `x` (in radians) |
    | :angle([Vector3D](vector3d.md) `x`) | float | Returns the angle (in radians) between this vector and `x` |
    | :distance([Vector3D](vector3d.md) `x`) | float | Returns the distance between this vector and `x` |
    | :toDegrees() | [Vector3D](vector3d.md) | Converts the vector from radians to degrees |
    | :toRadians() | [Vector3D](vector3d.md) | Converts the vector from degrees to radians |
    | :toStr() | String | Returns a string representation of the vector |