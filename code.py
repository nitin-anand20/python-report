import socket
import threading

# ===================== CONFIGURATION =====================
HOST = '127.0.0.1'  # Server IP
PORT = 5000         # Server Port

# ===================== SERVER =====================
clients = []
usernames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f'{username} left the chat.'.encode('utf-8'))
            usernames.remove(username)
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server started on {HOST}:{PORT}")
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        client.send('USERNAME'.encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)
        print(f'Username of the client is {username}')
        broadcast(f'{username} joined the chat!'.encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# ===================== CLIENT =====================
def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'USERNAME':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print('An error occurred!')
            client.close()
            break

def start_client():
    global username
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    username = input('Enter your username: ')

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    while True:
        message = f'{username}: {input()}'
        client.send(message.encode('utf-8'))

# ===================== MAIN =====================
mode = input("Enter mode (server/client): ").strip().lower()
if mode == 'server':
    start_server()
elif mode == 'client':
    start_client()
else:
    print("Invalid mode. Enter 'server' or 'client'.")
