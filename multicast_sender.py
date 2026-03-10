import socket
import time

MULTICAST_GROUP = '239.0.0.1'
PORT = 11000
MESSAGE = "UDP MULTICAST"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 1)

print("Multicast sender started")

while True:
    try:
        sock.sendto(MESSAGE.encode(), (MULTICAST_GROUP, PORT))
        print("Message sent")
        time.sleep(3)
    except KeyboardInterrupt:
        print("\nSender stopped.")
        break
    except Exception as e:
        print(f"Error: {e}")
