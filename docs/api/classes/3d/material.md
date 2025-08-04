=== "Constructors"

    | Function | Description |
    | - | - |
    | Material.new() | Creates a blank material |
    | Material.new([Texture](texture.md) `texture`) | Creates a material with an initial texture |
    | Material.new(Material `other`) | Creates a copy of another material |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .type | int | Material type |
    | .fog | bool | Enable/disable fog |
    | .backfaceCulling | bool | Enable/disable backface culling |
    | .frontfaceCulling | bool | Enable/disable frontface culling |
    | .antiAliasing | int | Anti-aliasing mode |
    | .wireframe | bool | Render in wireframe mode |
    | .diffuseColor | [Vector4D](vector4d.md) | Diffuse color |
    | .emissiveColor | [Vector4D](vector4d.md) | Emissive color |
    | .specularColor | [Vector4D](vector4d.md) | Specular color |
    | .gouradShading | bool | Enable/disable Gouraud shading |
    | .zWrite | bool | Enable/disable Z-buffer writing |
    | .zComparison | int | Z-buffer comparison mode |
    | .pointCloud | bool | Enable point cloud rendering |
    | .bilinearFiltering | bool | Enable bilinear filtering |
    | .trilinearFiltering | bool | Enable trilinear filtering |
    | .anisotropicFiltering | bool | Enable anisotropic filtering |
    | .shininess | float | Shininess factor |
    | .lighting | bool | Enable lighting (Legacy Drawing Only) |
    | .mipmaps | bool | Enable mipmapping |
    | .ID | int | Material ID |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :getTextureTranslation(int `layer`) | [Vector2D](vector2d.md) | Returns the UV offset for the specified texture layer |
    | :setTextureTranslation([Vector2D](vector2d.md) `offset`, int `layer`) |  | Sets the UV offset for the specified texture layer |
    | :getTextureScale(int `layer`) | [Vector2D](vector2d.md) | Returns the texture scale for the given layer (**currently always returns an empty vector**) |
    | :setTextureScale([Vector2D](vector2d.md) `scaling`, int `layer`) |  | Sets the texture scaling for the specified layer |
    | :setTextureUVWrapping(int `layer`, int `type`) |  | Sets wrapping type for U and V axes |
    | :setTextureUWrapping(int `layer`, int `type`) |  | Sets U-axis texture wrapping |
    | :setTextureVWrapping(int `layer`, int `type`) |  | Sets V-axis texture wrapping |
    | :setTexture([Texture](texture.md) `texture`, int `slot`) |  | Sets the texture for the given slot |
    | :setMaterialFlag(int `flag`, bool `enable`) |  | Enables or disables a material flag (see `irrlicht.MATERIAL_FLAG`) |