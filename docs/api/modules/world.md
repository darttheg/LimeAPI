=== "Functions"

    > **Note**: Functions with a ⚠️ must be invoked prior to window creation to take effect.

    | Function | Returns | Description |
    | - | - | - |
    | World.SetSkydome([Texture][texture] `sky`) |  | Sets the texture of the skydome |
    | World.SetSkydomeParameters(int `resX`, int `resY`, float `texturePercent`, float `spherePercent`, float `radius`) |  | Sets additional skydome parameters |
    | World.SetBackgroundColor([Vector4D][vector4d] `color`) |  | Sets world background color |
    | World.GetObjectCount() | int | Returns number of Irrlicht objects in the world |
    | World.FireRaypick3D([Vector3D][vector3d] `start`, [Vector3D][vector3d] `end`, float `debugLifeTime`) | Lua table | Fires a ray from start to end. Returns: `{ ID = int, normal = Vector3D, materialID = int, hitPosition = Vector3D }`. On failure: IDs = -1, normal = upward vector, hitPosition = `end` |
    | World.FireRaypick2D([Vector2D][vector2d] `screenCoord`, [Vector3D][vector3d] `end`) | Lua table | Fires a ray from screen space to 3D world position. Return is identical to `FireRaypick3D` |
    | World.SetFogDistances([Vector2D][vector2d] `distances`) |  | Sets fog start and end distances |
    | World.SetFogColor([Vector4D][vector4d] `color`) |  | Sets fog color |
    | World.SetFogDensity(float `density`) |  | Sets fog density |
    | World.SetFogType(int `type`) |  | Sets fog type |
    | World.SetPixelFog(bool `enable`) |  | Enables per-pixel fog |
    | World.SetRangeFog(bool `enable`) |  | Enables range-based fog (more expensive) |
    | World.SetFogParameters([Vector2D][vector2d] `distances`, [Vector4D][vector4d] `color`, int `type`, float `density`, bool `doPixelFog`, bool `doRangeFog`) |  | Sets all fog parameters in one call |
    | World.SetAmbientColor([Vector4D][vector4d] `color`) |  | Sets ambient lighting color |
    | World.ConvertToScreenPosition([Vector3D][vector3d] `position`) | [Vector2D][vector2d] | Converts 3D world position to 2D screen position |
    | World.SetShadows(bool `enable`) ⚠️ |  | Enables or disables shadows |
    | World.GetRenderTexture([Camera][camera] `camera`, [Vector2D][vector2d] `size`, bool `renderGUI`) | [Texture][texture] | Returns a texture of the camera’s view of the scene with optional GUI rendering |
    | World.Clear(bool `wipeCaches`) |  | Removes all 3D components; if `wipeCaches` is true, clears all mesh caches |
    | World.SetDefaultShadowFiltering(int `mode`) |  | Sets default shadow filtering; see [SHADOW_FILTER_SAMPLING][shadow_filter_sampling] |
    | World.SetDefaultShadowResolution(int `res`) |  | Sets default shadow resolution; see [SHADOW_RESOLUTION][shadow_resolution] |
    | World.SetDefaultLightingExclusion(bool `exclude`) |  | Sets whether new objects are excluded from lighting |
    | World.PreloadMesh(String `filePath`) |  | Preloads a mesh from file path |
    | World.PreloadTexture(String `filePath`) |  | Preloads a texture from file path |
    | World.UnloadMesh(String `filePath`) |  | Frees memory for a mesh from cache |
    | World.UnloadTexture(String `filePath`) |  | Frees memory for a texture from cache |
    | World.SetLegacyDrawing(bool `enable`) |  | If enabled, xEffects lighting and shadows are ignored |
    | World.SetShadowColor([Vector4D][vector4d] `color`) |  | Sets legacy shadow color |
    | World.SetShadowOpacity(int `opacity`) |  | Sets legacy shadow opacity |
    | World.SetLightManagementMode(int `mode`) |  | Sets light management mode; see [LIGHT_MANAGEMENT_MODE][light_management_mode]:<br>• `Distance to Camera` – default; closest 8 lights to camera<br>• `Nearest to Object` – 3 closest to object<br>• `Zone` – lights only affect objects under the same `Empty` |

[shadow_filter_sampling]: https://darttheg.github.io/LimeAPI/api/structs.html#shadow_filter_sampling
[shadow_resolution]: https://darttheg.github.io/LimeAPI/api/structs.html#shadow_resolution
[light_management_mode]: https://darttheg.github.io/LimeAPI/api/structs.html#light_management_mode

[vector2d]: https://darttheg.github.io/LimeAPI/api/classes/vector2d.html
[vector3d]: https://darttheg.github.io/LimeAPI/api/classes/vector3d.html
[vector4d]: https://darttheg.github.io/LimeAPI/api/classes/vector4d.html
[texture]: https://darttheg.github.io/LimeAPI/api/classes/texture.html
[camera]: https://darttheg.github.io/LimeAPI/api/classes/3d/camera.html