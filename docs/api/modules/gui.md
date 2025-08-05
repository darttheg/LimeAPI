=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | GUI.ImportFont(String `path`) |  | Imports a bitmap font from `path` |
    | GUI.SetDefaultFont(String `fontName`) |  | Sets the default font for new GUI elements (must already be imported) |
    | GUI.SetBilinearFiltering(bool `enable`) |  | Enables/disables bilinear filtering |
    | GUI.SetAnisotropicFiltering(bool `enable`) |  | Enables/disables anisotropic filtering |
    | GUI.SetTrilinearFiltering(bool `enable`) |  | Enables/disables trilinear filtering |
    | GUI.SetAntiAliasing(int `type`) |  | Sets anti-aliasing mode; see [ANTI_ALIASING_MODE][anti_aliasing_mode] |
    | GUI.Clear() |  | Removes all GUI components in Irrlicht |
    | GUI.Queue() |  | Queues GUI to render within the camera rendering queue |

[anti_aliasing_mode]: https://darttheg.github.io/LimeAPI/api/structs.html#anti_aliasing_mode