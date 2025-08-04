> **Note**: Peers do not receive information about other peers unless the server explicitly provides it. Clients **do not** receive `OnClientConnect` or `OnClientDisconnect` callbacks.

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | NetworkClient.Initialize() |  | Initializes the ENet library (shared with server) |
    | NetworkClient.SetVerbose(bool `enable`) |  | Enables/disables verbose logging (shared with server) |
    | NetworkClient.Create(int `maxConnections`, int `maxChannels`) |  | Creates a networking client with max allowed outgoing connections and channels (**`maxChannels` must match server’s**) |
    | NetworkClient.Destroy() |  | Destroys the client |
    | NetworkClient.Connect(String `IP`, int `port`, int `channelCount`) |  | Attempts to connect to a server at `IP:port` using `channelCount` channels (**uses min of client/server channel count**) <br>On success: `NetworkClient.OnConnect()` <br>On failure: `NetworkClient.OnConnectFail()` <br>Server receives: `NetworkServer.OnClientConnect(int peerID, int hostAddress)` |
    | NetworkClient.Disconnect() |  | Disconnects the client <br>Triggers: `NetworkClient.OnDisconnect(int reasonCode)` <br>Server receives: `NetworkServer.OnClientDisconnect(int peerID, int hostAddress)` |
    | NetworkClient.IsConnected() | bool | Returns whether the client is connected to a server |
    | NetworkClient.SendPacketToPeer(int `peerID`, int `channel`, [Packet](packet.md) `packet`, bool `TCP`) |  | Sends `packet` to a specific peer on specified channel via UDP/TCP |
    | NetworkClient.SendPacketToServer(int `channel`, [Packet](packet.md) `packet`, bool `TCP`) |  | Sends `packet` to the server on specified channel via UDP/TCP <br>Server receives: `NetworkServer.OnPacketReceived(int channel, [Packet](packet.md) packet)` |