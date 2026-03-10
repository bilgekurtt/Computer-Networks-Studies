import socket
import threading
import time

TCP_IP = "127.0.0.1"  #server ip
TCP_PORT = 22000

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #create tcp socket
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #allow reuse of the port
server_sock.bind((TCP_IP, TCP_PORT))  #bind to ip and port
server_sock.listen(5)  #allow up to 5 pending connections

print(f"TCP Simulated Multicast Server listening on {TCP_IP}:{TCP_PORT}...")

#dictionary to store clients by group letter
groups = {}  #key: group letter, value: list of client sockets
lock = threading.Lock()  #lock to protect shared groups dict

def handle_client(client_sock):
    try:
        #ask for group letter
        client_sock.send("GROUP: ".encode())
        group = client_sock.recv(1024).decode().strip().upper()

        with lock:
            if group not in groups:
                groups[group] = []
            groups[group].append(client_sock)

        print(f"Client joined group {group}")

        while True:
            time.sleep(1)  #keep the thread alive
            #the server sends messages every 3 seconds globally (handled separately)

    except Exception as e:
        print(f"Client error: {e}")
    finally:
        with lock:
            if group in groups and client_sock in groups[group]:
                groups[group].remove(client_sock)
        client_sock.close()
        print(f"Client disconnected from group {group}")

def multicast_sender():
    while True:
        time.sleep(3)
        with lock:
            for group, clients in groups.items():
                message = f"TCP SIMULATED MULTICAST GROUP {group}"
                for client in clients:
                    try:
                        client.send(message.encode())
                    except:
                        clients.remove(client)

try:
    sender_thread = threading.Thread(target=multicast_sender, daemon=True)
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