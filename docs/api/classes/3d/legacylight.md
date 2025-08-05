> **Note:** This class is only compatible with **Legacy Drawing**.

=== "Constructors"

    | Function | Description |
    | - | - |
    | LegacyLight.new() | Creates a default legacy light |
    | LegacyLight.new(LegacyLight `other`) | Creates a copy of another legacy light |
    | LegacyLight.new(int `type`) | Creates a light of specified type, see [LEGACY_LIGHT_TYPE][legacy_light_type] |
    | LegacyLight.new([Vector3D](vector3d.md) `position`) | Creates a light at the specified `position` |
    | LegacyLight.new(int `type`, [Vector3D](vector3d.md) `position`, [Vector3D](vector3d.md) `rotation`, [Vector4D](vector4d.md) `color`) | Full constructor with type, transform, and color |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector3D](vector3d.md) | Light position |
    | .rotation | [Vector3D](vector3d.md) | Light rotation |
    | .type | int | Light type, see [LEGACY_LIGHT_TYPE][legacy_light_type] |
    | .radius | float | Light radius |
    | .cones | [Vector2D](vector2d.md) | Inner and outer cone angles |
    | .attenuation | [Vector3D](vector3d.md) | Attenuation factors (constant, linear, quadratic) |
    | .falloff | float | Light falloff intensity |
    | .diffuseColor | [Vector4D](vector4d.md) | Diffuse (main) color |
    | .ambientColor | [Vector4D](vector4d.md) | Ambient color |
    | .specularColor | [Vector4D](vector4d.md) | Specular highlight color |
    | .debug | bool | Enable/disable debug visualization |
    | .active | bool | Whether the light is active in rendering |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :destroy() |  | Destroys the object |
    | :setParent(3DObject `other`) |  | Parents this light to another 3D object |
    | :getAbsolutePosition() | [Vector3D](vector3d.md) | Returns world position |
    | :getAbsoluteRotation() | [Vector3D](vector3d.md) | Returns world rotation |
    | :getAbsoluteScale() | [Vector3D](vector3d.md) | Returns world scale |
    | :updateAbsolutePosition() |  | Updates world transform (non-recursive) |

[legacy_light_type]: https://darttheg.github.io/LimeAPI/api/structs.html#legacy_light_type