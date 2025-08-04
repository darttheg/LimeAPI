=== "Constructors"

    | Function | Description |
    | - | - |
    | Image2D.new([Texture](texture.md) `texture`) | Creates an image from a texture |
    | Image2D.new([Texture](texture.md) `texture`, [Vector2D](vector2d.md) `position`) | Creates an image with texture and position |
    | Image2D.new([Texture](texture.md) `texture`, [Vector2D](vector2d.md) `position`, [Vector2D](vector2d.md) `size`) | Creates an image with texture, position, and size |
    | Image2D.new(Image2D `other`) | Creates a copy of another Image2D |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector2D](vector2d.md) | Image position |
    | .visible | bool | Image visibility |
    | .size | [Vector2D](vector2d.md) | Image size |
    | .scaleToFit | bool | Scale image to fit (**May need verification if functional**) |
    | .color | [Vector4D](vector4d.md) | Image color |
    | .hovered | bool | True if mouse is over the image |
    | .pressed | bool | True if image is being pressed |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :load([Texture](texture.md) `texture`) | | Loads a new texture |
    | :destroy() | | Destroys the object |
    | :setMaxSize([Vector2D](vector2d.md) `maxSize`) | | Sets max display size; crops image beyond `maxSize` |
    | :toFront() | | Moves image to the top of the z-order |
    | :toBack() | | Moves image to the back of the z-order |
    | :setBorderAlignment(int `left`, int `right`, int `top`, int `bottom`) | | Sets image border alignment (see `irrlicht.GUI_ALIGNMENT`) |
    | :setParent(Image2D `other`) | | Parents this image to another `Image2D` |
    | :fireOnClick(Function `f`) | | Binds function `f`, called with a bool when image is pressed/released |
    | :fireOnHover(Function `f`) | | Binds function `f`, called with a bool when mouse hovers/unhovers |