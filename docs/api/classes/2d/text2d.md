=== "Constructors"

    | Function | Description |
    | - | - |
    | Text2D.new() | Creates an empty Text2D |
    | Text2D.new(String `text`) | Creates a Text2D with initial text |
    | Text2D.new(String `text`, [Vector2D](vector2d.md) `position`) | Creates a Text2D at `position` with text |
    | Text2D.new(String `text`, [Vector2D](vector2d.md) `position`, [Vector2D](vector2d.md) `dimensions`) | Creates a Text2D at `position` with text and dimensions |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector2D](vector2d.md) | Text2D position |
    | .text | String | Text content |
    | .visible | bool | Text2D visibility |
    | .size | [Vector2D](vector2d.md) | Copy of Text2D size |
    | .wrap | bool | Enable/disable word wrap |
    | .textColor | [Vector4D](vector4d.md) | Text color |
    | .backgroundColor | [Vector4D](vector4d.md) | Background color |
    | .drawBorder | bool | Draw text box border |
    | .hovered | bool | True if mouse is over the text |
    | .pressed | bool | True if text is being pressed |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :destroy() |  | Destroys the object |
    | :setFont() |  | Sets the font to use |
    | :setMaxSize() |  | Sets the max visible size; crops beyond it |
    | :toFront() |  | Moves the Text2D to the top of the z-order |
    | :toBack() |  | Moves the Text2D to the back of the z-order |
    | :setBorderAlignment(int `left`, int `right`, int `top`, int `bottom`) |  | Sets border alignment, see [GUI_ALIGNMENT][gui_alignment] |
    | :setParent([Image2D](image2d.md) `image`) |  | Parents this Text2D to the given image |
    | :fireOnClick(Function `f`) |  | Binds function `f` with a bool indicating press/release |
    | :fireOnHover(Function `f`) |  | Binds function `f` with a bool indicating hover/unhover |

[gui_alignment]: https://darttheg.github.io/LimeAPI/api/structs.html#gui_alignment