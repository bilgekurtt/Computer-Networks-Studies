import socket
import threading

#server settings
HOST = "0.0.0.0"  #listen on all network interfaces
PORT = 12345

#keep track of connected clients and usernames
clients = []
usernames = []

#function to broadcast a message to all clients except sender
def broadcast(message, sender_sock):
    for client in clients:
        if client != sender_sock:
            try:
                client.send(message)
            except:
                clients.remove(client)

#handle a single client
def handle_client(client_sock):
    try:
        #ask for a username
        while True:
            client_sock.send("USERNAME: ".encode())
            username = client_sock.recv(1024).decode().strip()
            if username in usernames:
                client_sock.send("USERNAME_TAKEN\n".encode())
            else:
                usernames.append(username)
                clients.append(client_sock)
                client_sock.send(f"WELCOME {username}!\n".encode())
                broadcast(f"{username} joined the chat\n".encode(), client_sock)
                break

        #listen for messages
        while True:
            message = client_sock.recv(1024)
            if not message:
                break
            broadcast(f"{username}: {message.decode()}".encode(), client_sock)
    except:
        pass
    finally:
        #cleanup on disconnect
        if client_sock in clients:
            clients.remove(client_sock)
        if username in usernames:
            usernames.remove(username)
            broadcast(f"{username} left the chat\n".encode(), client_sock)
        client_sock.close()

#main server function
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Chat server started on port {PORT}...")

    while True:
        client_sock, addr = server.accept()
        print(f"Connection from {addr}")
        thread = threading.Thread(target=handle_client, args=(client_sock,)) #background threads
        thread.start()

if __name__ == "__main__":
    main()
