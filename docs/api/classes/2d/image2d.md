=== "Constructors"

    | Function | Description |
    | - | - |
    | Image2D.new([Texture][texture] `texture`) | Creates an image from a texture |
    | Image2D.new([Texture][texture] `texture`, [Vector2D][vector2d] `position`) | Creates an image with texture and position |
    | Image2D.new([Texture][texture] `texture`, [Vector2D][vector2d] `position`, [Vector2D][vector2d] `size`) | Creates an image with texture, position, and size |
    | Image2D.new(Image2D `other`) | Creates a copy of another Image2D |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector2D][vector2d] | Image position |
    | .visible | bool | Image visibility |
    | .size | [Vector2D][vector2d] | Image size |
    | .scaleToFit | bool | Scale image to fit (**May need verification if functional**) |
    | .color | [Vector4D][vector4d] | Image color |
    | .hovered | bool | True if mouse is over the image |
    | .pressed | bool | True if image is being pressed |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :load([Texture][texture] `texture`) | | Loads a new texture |
    | :destroy() | | Destroys the object |
    | :setMaxSize([Vector2D][vector2d] `maxSize`) | | Sets max display size; crops image beyond `maxSize` |
    | :toFront() | | Moves image to the top of the z-order |
    | :toBack() | | Moves image to the back of the z-order |
    | :setBorderAlignment(int `left`, int `right`, int `top`, int `bottom`) | | Sets image border alignment, see [GUI_ALIGNMENT][gui_alignment] |
    | :setParent(Image2D `other`) | | Parents this image to another `Image2D` |
    | :fireOnClick(Function `f`) | | Binds function `f`, called with a bool when image is pressed/released |
    | :fireOnHover(Function `f`) | | Binds function `f`, called with a bool when mouse hovers/unhovers |

[gui-alignment]: https://darttheg.github.io/LimeAPI/api/structs.html#gui_alignment

[vector2d]: https://darttheg.github.io/LimeAPI/api/classes/vector2d.html
[vector4d]: https://darttheg.github.io/LimeAPI/api/classes/vector4d.html
[texture]: https://darttheg.github.io/LimeAPI/api/classes/texture.html