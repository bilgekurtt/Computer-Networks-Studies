import socket
import time

TCP_IP = "127.0.0.1"  #server ip
TCP_PORT = 20000
MESSAGE = "TCP UNICAST"

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #create tcp socket

try:
    client_sock.connect((TCP_IP, TCP_PORT))  #connect to the receiver
    print(f"Connected to receiver at {TCP_IP}:{TCP_PORT}")

    while True:
        client_sock.send(MESSAGE.encode())  #send message
        print(f"Sent: {MESSAGE}")
        time.sleep(3)  #wait 3 seconds before sending next message

except KeyboardInterrupt:
    print("Sender stopped")

except Exception as e:
    print(f"Error: {e}")

finally:
    client_sock.close()  #close client socket