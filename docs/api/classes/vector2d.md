=== "Constructors"

    | Function | Description |
    | - | - |
    | Vector2D.new() | Creates a default Vector2D (0, 0) |
    | Vector2D.new(float `x`, float `y`) | Creates a Vector2D with `x` and `y` components |
    | Vector2D.new(float `x`) | Creates a Vector2D with both components set to `x` |

=== "Operations"

    | Operator | Description |
    | - | - |
    | `==` | Checks equality between two Vector2D objects |
    | `+` | Adds two Vector2D objects |
    | `-` | Subtracts one Vector2D from another |
    | `*` | Multiplies a Vector2D by a scalar |
    | `/` | Divides a Vector2D by a scalar |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :length() | float | Returns the length (magnitude) of the Vector2D |
    | :normalize() | [Vector2D](vector2d.md) | Returns a normalized Vector2D in range [0, 1] |
    | :normalizeToRange(float `x`, float `y`) | [Vector2D](vector2d.md) | Returns a Vector2D normalized to the range [`x`, `y`] |
    | :dot([Vector2D](vector2d.md) `x`) | float | Returns the dot product with vector `x` |
    | :rotate(float `x`) | [Vector2D](vector2d.md) | Returns the vector rotated by `x` radians |
    | :angle([Vector2D](vector2d.md) `x`) | float | Returns the angle between this vector and `x` |
    | :distance([Vector2D](vector2d.md) `x`) | float | Returns the distance between this vector and `x` |
    | :toStr() | String | Returns a string representation of the vector |