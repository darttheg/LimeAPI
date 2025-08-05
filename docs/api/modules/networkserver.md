=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | NetworkServer.Initialize() |  | Initializes the ENet library (shared with client) |
    | NetworkServer.SetVerbose(bool `enable`) |  | Enables/disables verbose logging (shared with client) |
    | NetworkServer.Host(String `IP`, int `port`, int `maxPeers`, int `maxChannels`) |  | Attempts to host on `IP:port` with `maxPeers` and `maxChannels` channels (0–maxChannels) <br>On success: `NetworkServer.OnHosted()` <br>On failure: `NetworkServer.OnHostFail()` |
    | NetworkServer.IsHosting() | bool | Returns whether the server is currently hosting |
    | NetworkServer.StopHosting() |  | Stops the hosted server |
    | NetworkServer.GetIP() | String | Returns the IP address of the hosted server |
    | NetworkServer.GetPort() | int | Returns the port of the hosted server |
    | NetworkServer.SetBandwidthLimits(int `incomingLimit`, int `outgoingLimit`) |  | Sets bandwidth limits in bytes/sec (0 = unlimited) |
    | NetworkServer.Shutdown() |  | Shuts down ENet and disconnects from all peers |
    | NetworkServer.GetPeerState(int `peerID`) | int | Returns state of peer; see [PEER_STATE][peer_state] |
    | NetworkServer.GetPeerPing(int `peerID`) | int | Returns ping time of peer in milliseconds |
    | NetworkServer.DisconnectPeer(int `peerID`, int `reasonCode`) |  | Forcefully disconnects peer with `reasonCode` <br>Client receives: `NetworkClient.OnDisconnect(int reasonCode)` |
    | NetworkServer.SendPacketToPeer(int `peerID`, int `channel`, [Packet][packet] `packet`, bool `TCP`) |  | Sends `packet` to a peer over specified channel and protocol <br>Client receives: `NetworkClient.OnPacketReceived(int channel, [Packet][packet] packet)` |
    | NetworkServer.SendPacketToAll(int `channel`, [Packet][packet] `packet`, bool `TCP`) |  | Sends `packet` to all peers on the specified channel <br>Clients receive: `NetworkClient.OnPacketReceived(int channel, [Packet][packet] packet)` |

[peer_state]: https://darttheg.github.io/LimeAPI/api/structs.html#peer_state
[packet]: https://darttheg.github.io/LimeAPI/api/classes/packet.html