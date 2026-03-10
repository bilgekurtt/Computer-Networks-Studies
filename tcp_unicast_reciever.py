import socket

TCP_IP = "127.0.0.1"  #listen on localhost
TCP_PORT = 20000

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #create tcp socket
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #allow reuse of the port
server_sock.bind((TCP_IP, TCP_PORT))  #bind to ip and port
server_sock.listen(1)  #only one connection at a time

print(f"TCP Unicast Receiver listening on {TCP_IP}:{TCP_PORT}...")

try:
    client_sock, addr = server_sock.accept()  #accept a client connection
    print(f"Connected by {addr}")

    while True:
        data = client_sock.recv(1024)  #receive data from client
        if not data:
            break
        print(f"Received: {data.decode()}")

except KeyboardInterrupt:
    print("Receiver stopped")

except Exception as e:
    print(f"Error: {e}")

finally:
    client_sock.close()  #close client socket
    server_sock.close()  #close server socket