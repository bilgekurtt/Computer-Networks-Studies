import socket
import time

#destination ip and which port reciever is listening
UDP_IP = "127.0.0.1"
UDP_PORT = 10000
MESSAGE = "UDP UNICAST"

#create socket, with IPv4, using UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    #keep sending messages
    while True:
        #turn string to bytes and send to reciever (IP:Port)
        sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
        print(f"Sent: {MESSAGE}")
        time.sleep(3)
except KeyboardInterrupt:
    print("Sender stopped")
except Exception as e:
    print(f"Error: {e}")
finally:
    sock.close()
