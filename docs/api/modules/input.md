=== "Invoked by Engine"

    | Function | When | Description |
    | - | - | - |
    | Input.OnLeftMouseClick() | On left click | Left mouse click function |
    | Input.OnRightMouseClick() | On right click | Right mouse click function |
    | Input.OnMiddleMouseClick() | On middle click | Middle mouse click function |
    | Input.OnMouseMove([Vector2D](vector2d.md) `position`) | On mouse move | Mouse move function |
    | Input.OnMouseScroll(float `wheelDelta`) | On scroll | Mouse scroll function |
    | Input.OnKeyPressed(int `key`) | On key press | On key pressed function |
    | Input.OnKeyReleased(int `key`) | On key release | On key released function |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | Input.IsKeyDown(int `key`) | bool | Returns whether the key is currently pressed |
    | Input.GetMouseState() | Lua table | Returns `{ position = Vector2D, leftDown = bool, rightDown = bool, middleDown = bool, wheelDelta = float }` |
    | Input.GetControllerState() | Lua table | Returns `{ axis = table, buttons = table }` |
    | Input.CheckControllers() |  | Checks for connected/disconnected controllers |
    | Input.SetMouseVisibility(bool `visible`) |  | Sets whether the mouse cursor is visible |
    | Input.SetMousePosition([Vector2D](vector2d.md) `position`) |  | Sets the position of the mouse cursor |