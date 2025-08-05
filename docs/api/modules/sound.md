=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | Sound.PlaySound2D(String `path`, bool `loop`) | int | Plays a 2D sound and returns the channel used |
    | Sound.PlaySound3D(String `path`, [Vector3D](vector3d.md) `position`, bool `loop`) | int | Plays a 3D sound and returns the channel used |
    | Sound.PlaySound2DOnChannel(int `channel`, String `path`, bool `loop`) |  | Plays a 2D sound on a specific channel |
    | Sound.PlaySound3DOnChannel(int `channel`, String `path`, [Vector3D](vector3d.md) `position`, bool `loop`) |  | Plays a 3D sound on a specific channel |
    | Sound.StopChannel(int `channel`) |  | Stops the sound on the specified channel |
    | Sound.StopAllChannels() |  | Stops all currently playing sounds |
    | Sound.SetChannelPaused(int `channel`, bool `pause`) |  | Pauses or resumes the channel |
    | Sound.SetChannelLooped(int `channel`, bool `loop`) |  | Sets whether the channel loops |
    | Sound.PreloadSound(String `path`) |  | Preloads the sound file into memory |
    | Sound.SetListenerPosition([Vector3D](vector3d.md) `position`, [Vector3D](vector3d.md) `forward`) |  | Sets 3D listener position and forward direction |
    | Sound.SetChannelPosition3D(int `channel`, [Vector3D](vector3d.md) `position`) |  | Sets 3D position of a sound on the channel |
    | Sound.SetChannelMinimumDistance(int `channel`, float `distance`) |  | Sets minimum distance for full volume on a 3D sound |
    | Sound.ClearChannelEffects(int `channel`) |  | Removes all effects applied to the channel |
    | Sound.SetChannelEffect(int `channel`, int `effect`, bool `enable`, table `parameters`) |  | Enables/disables a sound effect, see [SOUND_EFFECT][sound_effect].<br><br>`DISTORTION` – `{ gain = float, edge = float }`<br>`ECHO` – `{ wetDry = float, feedback = float, delay = float }`<br>`REVERB` – `{ inputGain = float, reverbMix = float, reverbTime = float, frequencyRatio = float }`<br>`PARAMEQ` – `{ frequency = float, bandwidth = float, gain = float }`<br>`GARGLE` – `{ rate = float, sinusWaveForm = bool }` |
    | Sound.SetChannelVolume(int `channel`, int `volume`) |  | Sets the volume of the channel |
    | Sound.SetChannelPitch(int `channel`, float `pitch`) |  | Sets the pitch of the sound |
    | Sound.SetChannelPan(int `channel`, float `pan`) |  | Sets the stereo pan of the sound |
    | Sound.GetChannelList() | Lua table | Returns `{ [channelID] = soundPath }` |
    | Sound.SetChannelPlaybackSpeed(int `channel`, float `speed`) |  | Sets playback speed for the channel |
    | Sound.SetChannelPlaybackPosition(int `channel`, int `milliseconds`) |  | Seeks to a position in milliseconds |
    | Sound.SetChannelVelocity(int `channel`, [Vector3D](vector3d.md) `velocity`) |  | Sets velocity for Doppler effect |
    | Sound.SetDopplerEffectParameters(float `dopplerFactor`, float `distanceFactor`) |  | Sets Doppler effect parameters. `dopplerFactor` ranges `0.0–10.0` (default `1.0`), `distanceFactor` defines meters per unit (default `1.0`; use `0.3048` for feet/sec) |
    | Sound.IsChannelEmpty(int `channel`) | bool | Returns true if no sound is playing on the channel |

[sound_effect]: https://darttheg.github.io/LimeAPI/api/structs.html#sound_effect