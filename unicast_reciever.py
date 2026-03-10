import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 10000

#create a socket, with IPv4, using UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#bind socket to the target IP:Port
sock.bind((UDP_IP, UDP_PORT))

print(f"Unicast receiver listening on {UDP_IP}:{UDP_PORT}...")

try:
    #constantly listen
    while True:
        #wait until data is recieved and save it and its addr
        data, addr = sock.recvfrom(1024)  #max 1024 bytes
        #turns bytes into string
        print(f"Received message from {addr}: {data.decode()}")
except KeyboardInterrupt:
    print("Receiver stopped")
except Exception as e:
    print(f"Error: {e}")
finally:
    sock.close()
