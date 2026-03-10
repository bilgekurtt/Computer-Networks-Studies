import socket
import threading
import time

TCP_IP = "127.0.0.1"  #server ip
TCP_PORT = 22200

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #create tcp socket
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #allow reuse of the port
server_sock.bind((TCP_IP, TCP_PORT))  #bind to ip and port
server_sock.listen(5)  #allow up to 5 pending connections

print(f"TCP Simulated Broadcast Server listening on {TCP_IP}:{TCP_PORT}...")

clients = []  #list of connected clients
lock = threading.Lock()  #lock to protect shared clients list

def handle_client(client_sock):
    try:
        with lock:
            clients.append(client_sock)
        print(f"New client connected: {client_sock.getpeername()}")

        while True:
            time.sleep(1)  #keep thread alive

    except Exception as e:
        print(f"Client error: {e}")
    finally:
        with lock:
            if client_sock in clients:
                clients.remove(client_sock)
        client_sock.close()
        print(f"Client disconnected: {client_sock.getpeername()}")

def broadcast_sender():
    while True:
        time.sleep(3)
        message = "TCP SIMULATED BROADCAST"
        with lock:
            for client in clients:
                try:
                    client.send(message.encode())
                except:
                    clients.remove(client)

try:
    sender_thread = threading.Thread(target=broadcast_sender, daemon=True)
    sender_thread.start()

    while True:
        client_sock, addr = server_sock.accept()
        print(f"Connection from {addr}")
        thread = threading.Thread(target=handle_client, args=(client_sock,), daemon=True)
        thread.start()

except KeyboardInterrupt:
    print("Server stopped")

except Exception as e:
    print(f"Server error: {e}")

finally:
    server_sock.close()
