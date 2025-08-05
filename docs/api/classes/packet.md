=== "Constructors"

    | Function | Description |
    | - | - |
    | Packet.new() | Creates a new, empty packet |

=== "Alterables"

    | Property | Type | Description |
    | - | - | - |
    | .ID | int | Sender ID (peer ID or server) |
    | .position | int | Current byte position used by `:getNext()` |

=== "Functions"

    | Function | Returns | Description |
    | - | - | - |
    | :append(int `dataType`, `data`) |  | Appends data of type `dataType` to the packet. See `irrlicht.DATA_TYPE`. For `FILE`, `data` should be a file path. |
    | :get(int `dataType`, int `bytePosition`) | any | Retrieves data of the specified type at the given byte position |
    | :getNext(int `dataType`) | any | Retrieves data at the current position and advances `.position` by `dataType` size |
    | :getSize() | int | Returns the size of the packet in bits |
    | :destroy() |  | Destroys the packet |
    | :writeToFile(int `bytePosition`, String `path`) |  | Writes data from `bytePosition` to `path` |