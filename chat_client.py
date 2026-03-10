import socket
import threading

#server settings
SERVER_IP = "127.0.0.1"  #local server
SERVER_PORT = 12345

#connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))

#function to receive messages
def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print("Connection closed by server.")
            break

#function to send messages
def send_messages():
    while True:
        msg = input()
        client.send(msg.encode())

#handle username
while True:
    msg = client.recv(1024).decode()
    if msg.startswith("USERNAME:"):
        username = input("Enter username: ")
        client.send(username.encode())
    elif msg.startswith("USERNAME_TAKEN"):
        print("Username already taken, try again.")
    else:
        print(msg)
        break

#start threads for sending and receiving messages
recv_thread = threading.Thread(target=receive_messages)
recv_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
