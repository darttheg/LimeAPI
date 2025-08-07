=== "Invoked by Engine"

    | Function | When | Description |
    | - | - | - |
    | Lime.OnStart() | On startup following running `main.lua` | The first function to be called by Lime |
    | Lime.OnUpdate(float `deltaTime`) | Every frame | Update function containing `deltaTime` |
    | Lime.OnEnd() | On end of life | The last function to be called by Lime |

=== "Functions"

    > **Note**: Functions with a ⚠️ must be invoked prior to window creation to take effect.

    | Function | Returns | Description |
    | - | - | - |
    | Lime.GetVersion() | String | Returns the current Lime version running |
    | Lime.SetDriverType(int `type`) ⚠️ |  | Set driver type to use |
    | Lime.SetFullscreen(bool `fullscreen`) |  | Set fullscreen or windowed mode |
    | Lime.SetMatchResolutionToSize(bool `match`) |  | Sets whether or not the Irrlicht rendering resolution should match the size of the window |
    | Lime.SetCaption(String `caption`) |  | Set window caption |
    | Lime.GetCaption() | String | Returns window caption text |
    | Lime.GetFrameRate() | int | Returns the current frame rate of the application |
    | Lime.SetFrameRate(int `fps`) |  | Sets the target frame rate |
    | Lime.GetMemoryUsage() | float | Returns application memory usage in megabytes |
    | Lime.SetWindowPosition([Vector2D][vector2d] `position`) |  | Set window position |
    | Lime.SetWindowSize([Vector2D][vector2d] `size`) |  | Set size of the application |
    | Lime.SetAutoAspectRatio(bool `enable`) | | Set whether or not Lime mains aspect ratio when resized |
    | Lime.GetWindowSize() | [Vector2D][vector2d] | Returns the size of the render window |
    | Lime.GetMonitorSize() | [Vector2D][vector2d] | Returns the size of the user's monitor |
    | Lime.EndApplication() |  | Ends the application |
    | Lime.IsWindowFocused() | bool | Returns whether the window is focused |
    | Lime.SetResizable(bool `allow`) |  | Sets whether the application should be resizable |
    | Lime.GetElapsedTime() | int | Returns elapsed runtime in milliseconds |
    | Lime.Log(String `message`) |  | Sends a message to the debug console |
    | Lime.AddArchiveToMemory(String `path`) |  | Adds archive from `path` to memory |
    | Lime.SetShowConsole(bool `show`) ⚠️ |  | Shows console |
    | Lime.SetWriteConsole(bool `write`) |  | Writes console output to `output.txt` |
    | Lime.SetVSync(bool `enable`) ⚠️ |  | Enables/disables vertical sync (*Irrlicht cannot update v-sync at runtime, but a workaround may be explored in the future*) |
    | Lime.DisplayMessage(String `title`, String `message`, int `icon`) |  | Displays a Windows pop-up message; see [MESSAGE_ICON][message_icon] |
    | Lime.RecreateDevice() | | Applies any window changes such as a change in driver type and creates a new window (**Currently crashes**)

[message_icon]: https://darttheg.github.io/LimeAPI/api/structs.html#message_icon

[vector2d]: https://darttheg.github.io/LimeAPI/api/classes/vector2d.html