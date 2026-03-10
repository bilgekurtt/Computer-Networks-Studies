# Computer Networks Studies

A collection of Python socket programming exercises exploring core networking concepts — unicast, multicast, and broadcast communication over both UDP and TCP protocols, along with a functioning multi-client chat room.

All scripts are designed to run locally and communicate over localhost or a local network.

## Contents

### UDP
| File | Description |
|------|-------------|
| `unicast_sender.py` / `unicast_reciever.py` | One-to-one UDP communication |
| `multicast_sender.py` / `multicast_reciever.py` | One-to-many UDP multicast using a multicast group address |
| `broadcast_sender.py` / `broadcast_reciever.py` | One-to-all UDP broadcast across the local network |

### TCP
| File | Description |
|------|-------------|
| `tcp_unicast_sender.py` / `tcp_unicast_reciever.py` | One-to-one TCP communication |
| `tcp_multicast_server.py` / `tcp_multicast_client.py` | Simulated multicast over TCP using client groups |
| `tcp_broadcast_server.py` / `tcp_broadcast_client.py` | Simulated broadcast over TCP to all connected clients |

### Chat Room
| File | Description |
|------|-------------|
| `chat_server.py` | Multi-client TCP chat server with username handling and broadcast messaging |
| `chat_client.py` | Chat client with concurrent send/receive using threads |

## How to Run

Each example requires two terminal windows — one for the sender/server and one for the receiver/client. For example:

**UDP Unicast:**
```bash
# Terminal 1
python unicast_reciever.py

# Terminal 2
python unicast_sender.py
```

**Chat Room:**
```bash
# Terminal 1 (start server first)
python chat_server.py

# Terminal 2+ (one per client)
python chat_client.py
```

The same pattern applies to all other examples — start the server or receiver first, then the sender or client.

## Concepts Covered

- UDP vs TCP — connectionless vs connection-oriented communication
- Unicast, multicast, and broadcast addressing
- Python `socket` module
- Multithreading for concurrent client handling
- Socket options (`SO_BROADCAST`, `IP_ADD_MEMBERSHIP`, `SO_REUSEADDR`)
