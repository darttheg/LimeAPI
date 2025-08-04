=== "Constructors"

    | Function | Description |
    | - | - |
    | MeshBuffer.new() | Creates an empty mesh buffer |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :pushFace([Vector3D](vector3d.md) `vertex1`, [Vector3D](vector3d.md) `vertex2`, [Vector3D](vector3d.md) `vertex3`, [Vector3D](vector3d.md) `normal1`, [Vector3D](vector3d.md) `normal2`, [Vector3D](vector3d.md) `normal3`, [Vector2D](vector2d.md) `uvw1`, [Vector2D](vector2d.md) `uvw2`, [Vector2D](vector2d.md) `uvw3`, [Vector4D](vector4d.md) `color1`, [Vector4D](vector4d.md) `color2`, [Vector4D](vector4d.md) `color3`) |  | Appends a new triangular face to the mesh buffer |
    | :clear() |  | Clears the data in the buffer |
    | :destroy() |  | Destroys the buffer |
    | :getVertexCount() | int | Returns the number of vertices in the buffer |