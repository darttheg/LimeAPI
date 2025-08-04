=== "Constructors"

    | Function | Description |
    | - | - |
    | Camera.new() | Creates a default camera |
    | Camera.new(Camera `x`) | Creates a copy of camera `x` |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector3D](vector3d.md) | Camera position |
    | .rotation | [Vector3D](vector3d.md) | Camera rotation |
    | .viewPlanes | [Vector2D](vector2d.md) | Near and far view planes |
    | .orthogonal | bool | Is the Camera orthogonal |
    | .fieldOfView | float | Set/get the field of view (degrees); for orthogonal cameras, .fieldOfView acts as a zoom scalar |
    | .visible | bool | Set/get camera visibility |
    | .aspectRatio | float | Camera aspect ratio |
    | .up | [Vector3D](vector3d.md) | Camera up vector |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :getForward() | [Vector3D](vector3d.md) | Returns the camera's forward direction |
    | :getLeft() | [Vector3D](vector3d.md) | Returns the camera's left direction |
    | :getAbsolutePosition() | [Vector3D](vector3d.md) | Returns the world position |
    | :setActive() | | Sets this camera as the active camera |
    | :queue(bool `legacy`) | | Queues this camera to render on top of the active one; `legacy` determines if xEffects are used |
    | :destroy() | | Destroys the object |