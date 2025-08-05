=== "Constructors"

    | Function | Description |
    | - | - |
    | EditBox.new() | Creates a default EditBox |
    | EditBox.new(String `text`) | Creates an EditBox with initial text |
    | EditBox.new(String `text`, [Vector3D](vector3d.md) `position`) | Creates an EditBox at `position` with text |
    | EditBox.new(String `text`, [Vector3D](vector3d.md) `position`, [Vector3D](vector3d.md) `dimensions`) | Creates an EditBox at `position` with text and size |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector2D](vector2d.md) | EditBox position |
    | .text | String | Text content |
    | .visible | bool | EditBox visibility |
    | .size | [Vector2D](vector2d.md) | Copy of EditBox size |
    | .wrap | bool | Enable/disable word wrap |
    | .textColor | [Vector4D](vector4d.md) | Text color |
    | .drawBorder | bool | Draw text box border |
    | .focused | bool | Whether the EditBox is focused |
    | .enabled | bool | Enable or disable the EditBox |
    | .password | bool | Obfuscate text like a password field |
    | .multiLine | bool | Allow multiline input |
    | .autoScroll | bool | Autoscroll to follow user input |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :destroy() |  | Destroys the object |
    | :setFont() |  | Sets the font to use |
    | :setMaxSize() |  | Sets the max visible size of the EditBox; crops beyond it |
    | :toFront() |  | Moves the EditBox to the top of the z-order |
    | :toBack() |  | Moves the EditBox to the back of the z-order |
    | :setBorderAlignment(int `left`, int `right`, int `top`, int `bottom`) |  | Sets border alignment, see [GUI_ALIGNMENT][gui_alignment] |
    | :setParent([Image2D](image2d.md) `image`) |  | Parents this EditBox to the given image |

[gui-alignment]: https://darttheg.github.io/LimeAPI/api/structs.html#gui_alignment