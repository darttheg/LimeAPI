=== "Constructors"

    | Function | Description |
    | - | - |
    | Texture.new() | Creates an empty texture |
    | Texture.new(String `path`) | Loads a texture from a file path |
    | Texture.new([Vector2D](vector2d.md) `size`) | Creates a blank texture with specified size |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :load(String `path`) |  | Loads a texture from the given path |
    | :toStr() | String | Returns the texture's path as a string |
    | :keyColor([Vector2D](vector2d.md) `position`) |  | Keys the color at the given position into transparency |
    | :save(String `path`) |  | Saves the texture to the specified file path |
    | :clear([Vector2D](vector2d.md) `size`) |  | Clears the texture and creates a blank one of the given size |
    | :append([Texture](texture.md) `texture`, [Vector2D](vector2d.md) `position`) |  | Appends another texture at the given position |
    | :appendFromFile(String `filePath`, [Vector2D](vector2d.md) `position`) |  | Appends texture data from file at the given position |
    | :getPixelColor([Vector2D](vector2d.md) `position`) | [Vector4D](vector4d.md) | Returns the color at the specified pixel position |