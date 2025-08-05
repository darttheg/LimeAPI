=== "Constructors"

    | Function | Description |
    | - | - |
    | ParticleSystem.new() | Creates a new particle system |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .position | [Vector3D](vector3d.md) | Particle system position |
    | .rotation | [Vector3D](vector3d.md) | Particle system rotation |
    | .scale | [Vector3D](vector3d.md) | Particle system scale |
    | .debug | bool | Enable/disable debug data |
    | .active | bool | Enable/disable updating |
    | .visible | bool | Set/get visibility |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :destroy() |  | Removes the particle system in Irrlicht |
    | :setParent(3DObject `other`) |  | Parents this 3D object to another |
    | :getAbsolutePosition() | [Vector3D](vector3d.md) | Returns world position |
    | :getAbsoluteRotation() | [Vector3D](vector3d.md) | Returns world rotation |
    | :getAbsoluteScale() | [Vector3D](vector3d.md) | Returns world scale |
    | :updateAbsolutePosition() |  | Updates world transform (non-recursive) |
    | :setDoAbsoluteTracking(bool `enable`) |  | Sets whether particles move relative to the object (default `true`) |
    | :loadMaterial([Material](material.md) `material`) |  | Loads material (**Must apply before setting emitter!**) |
    | :clearAffectors() |  | Clears all applied affectors |
    | :clearParticles() |  | Clears emitted particles |
    | :spark(int `particleAmount`) |  | Emits `particleAmount` particles instantly |
    | :setEmitter(int `emitterType`, table `parameters`) |  | Sets emitter type and parameters. See [PARTICLE_EMITTER_TYPE][particle_emitter_type]. Global fields: ` { position = Vector3D, velocity = Vector3D, maxAngle = float, lifeTime = Vector2D, particlesPerSecond = Vector2D, minStartingColor = Vector4D, maxStartingColor = Vector4D, startSize = Vector2D } ` Type-specific fields: `POINT (0)` – none, `CUBE (1)` – `{ minEdge = Vector3D, maxEdge = Vector3D }`, `SPHERE (2)` – `{ radius = float }`, `RING (3)` – `{ radius = float, thickness = float }` |
    | :addAffector(int `affectorType`, table `parameters`) |  | Adds a particle affector. See [PARTICLE_AFFECTOR_TYPE][particle_affector_type]. `ATTRACT (0)` – `{ attractPosition = Vector3D, attractAxis = Vector3D }`, `FADE_OUT (1)` – `{ targetColor = Vector4D, time = float }`, `GRAVITY (2)` – `{ gravity = Vector3D, timeToTakeOver = float }`, `ROTATION (3)` – `{ rotationSpeed = Vector3D }`, `SCALE (4)` – `{ scalar = Vector2D }` |

[particle_emitter_type]: https://darttheg.github.io/LimeAPI/api/structs.html#particle_emitter_type
[particle_affector_type]: https://darttheg.github.io/LimeAPI/api/structs.html#particle_affector_type