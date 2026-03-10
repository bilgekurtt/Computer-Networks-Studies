import socket
import struct

#multicast addr and port tot listen to
MULTICAST_GROUP = '239.0.0.1'
PORT = 11000

#create udp ssocket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

#let multiple sockets have the same port
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#bind all interfaces to the port
sock.bind(('', PORT))

#convert multicast ip to binary
group = socket.inet_aton(MULTICAST_GROUP)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
#add the socket to the multicast group
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print(f"Multicast receiver listening on {MULTICAST_GROUP}:{PORT}")

while True:
    try:
        data, addr = sock.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")
    except KeyboardInterrupt:
        print("\nReceiver stopped.")
        break
    except Exception as e:
        print(f"Error: {e}")
