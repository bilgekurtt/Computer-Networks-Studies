import socket
import threading

TCP_IP = "127.0.0.1"  #server ip
TCP_PORT = 22200

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #create tcp socket
client_sock.connect((TCP_IP, TCP_PORT))
print(f"Connected to server at {TCP_IP}:{TCP_PORT}")

#function to receive messages from server
def receive_messages():
    while True:
        try:
            message = client_sock.recv(1024).decode()
            if not message:
                break
            print(f"Received: {message}")
        except:
            print("Connection closed by server")
            break

recv_thread = threading.Thread(target=receive_messages, daemon=True)
recv_thread.start()
recv_thread.join()
client_sock.close()
