import socket

BROADCAST_IP = "0.0.0.0"  #listen on all interfaces
BROADCAST_PORT = 11100

#create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#allow multiple programs to bind to the same port
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#bind to the broadcast port
sock.bind((BROADCAST_IP, BROADCAST_PORT))

print(f"UDP Broadcast Receiver listening on port {BROADCAST_PORT}...")

try:
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")
except KeyboardInterrupt:
    print("Receiver stopped")
except Exception as e:
    print(f"Error: {e}")
finally:
    sock.close()