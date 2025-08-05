=== "Constructors"

    | Function | Description |
    | - | - |
    | Camera.new() | Creates a default camera |
    | Camera.new(Camera `x`) | Creates a copy of camera `x` |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector3D][vector3d] | Camera position |
    | .rotation | [Vector3D][vector3d] | Camera rotation |
    | .viewPlanes | [Vector2D][vector2d] | Near and far view planes |
    | .orthogonal | bool | Is the Camera orthogonal |
    | .fieldOfView | float | Set/get the field of view (degrees); for orthogonal cameras, .fieldOfView acts as a zoom scalar |
    | .visible | bool | Set/get camera visibility |
    | .aspectRatio | float | Camera aspect ratio |
    | .up | [Vector3D][vector3d] | Camera up vector |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :getForward() | [Vector3D][vector3d] | Returns the camera's forward direction |
    | :getLeft() | [Vector3D][vector3d] | Returns the camera's left direction |
    | :getAbsolutePosition() | [Vector3D][vector3d] | Returns the world position |
    | :setActive() | | Sets this camera as the active camera |
    | :queue(bool `legacy`) | | Queues this camera to render on top of the active one; `legacy` determines if xEffects are used |
    | :destroy() | | Destroys the object |

[vector2d]: https://darttheg.github.io/LimeAPI/api/classes/vector2d.html
[vector3d]: https://darttheg.github.io/LimeAPI/api/classes/vector3d.html
[vector4d]: https://darttheg.github.io/LimeAPI/api/classes/vector4d.html
[texture]: https://darttheg.github.io/LimeAPI/api/classes/texture.html