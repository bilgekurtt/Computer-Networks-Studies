import socket
import time

BROADCAST_IP = "255.255.255.255"  #broadcast to all hosts
BROADCAST_PORT = 11100
MESSAGE = "UDP BROADCAST"

#create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#enable broadcasting mode
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print(f"UDP Broadcast Sender started on {BROADCAST_IP}:{BROADCAST_PORT}")

try:
    while True:
        sock.sendto(MESSAGE.encode(), (BROADCAST_IP, BROADCAST_PORT))
        print(f"Sent: {MESSAGE}")
        time.sleep(3)
except KeyboardInterrupt:
    print("Sender stopped")
except Exception as e:
    print(f"Error: {e}")
finally:
    sock.close()
