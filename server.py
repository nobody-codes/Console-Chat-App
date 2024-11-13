
'''
import socket
import sys
import threading
import time

clients = []
user_names = []

# Create a Socket (connect two computers)
def create_socket():
    try:
        global host
        global port
        global server
        host = "0.0.0.0"
        port = 9999
        server = socket.socket()
    except socket.error as msg:
        print(f"Socket creation error: {str(msg)}")


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global server
        print("Binding the Port: " + str(port))

        server.bind((host, port))
        server.listen(5)

    except socket.error as msg:
        print(f"Socket Binding error {str(msg)} \n Retrying...")
        bind_socket()
        
def broadcast(message): # encoded parameter 
    for client in clients:
        client.send(message)
        
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            user_name = user_names[index]
            broadcast('{user_name} left!'.encode('ascii'))
            user_names.remove(user_name)
            break
        
        
def optimise_room():
    return 200, "optimise-room"

def self_optimise_conn():
    return 350, "self-optimise-conn"

# Send messages to client or a friend
def client_conn(conn): # conn -> client
    while True:
        # Request and Store User name
        conn.send('SUN'.encode('ascii'))
        user_name = conn.recv(1024).decode('ascii')
        user_names.append(user_name)
        clients.append(conn)

        # Print and Broadcast User name
        print("User Name is {}".format(user_name))
        broadcast("{} joined!".format(user_name).encode('ascii'))
        conn.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(conn,))
        thread.start()
        
def pass_conn_server():
    return 0, "pass-conn-server"


# Establish connection with a client (socket must be listening)
def socket_accept():
    try:
        conn, address = server.accept()
        print(f"Connection has been established! | IP {address[0]} | Port {str(address[1])}")
        client_conn(conn) # start chat with client 
        conn.close()
    except socket.error as msg:
        print(f"Socket Accecpting error {str(msg)} \n Retrying...")
        socket_accept()

def main():
    create_socket()
    bind_socket()
    socket_accept()

while True:
    main()
    
'''

import socket
import threading

clients = []
user_names = []

# Create a Socket (connect two computers)
def create_socket():
    try:
        global server
        host = "0.0.0.0"
        port = 9999
        server = socket.socket()
        server.bind((host, port))
        server.listen(5)
        print(f"Server is listening on port {port}")
    except socket.error as msg:
        print(f"Socket creation error: {str(msg)}")


def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            # Remove clients that can't be reached
            clients.remove(client)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if not message:
                raise Exception("Client disconnected")
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            user_name = user_names[index]
            broadcast(f'{user_name} left!'.encode('ascii'))
            user_names.remove(user_name)
            break

def client_conn(conn):
    conn.send('Enter your username:'.encode('ascii'))
    user_name = conn.recv(1024).decode('ascii')
    user_names.append(user_name)
    clients.append(conn)

    print(f"User Name is {user_name}")
    broadcast(f"{user_name} joined!".encode('ascii'))
    conn.send('Connected to server!'.encode('ascii'))

    thread = threading.Thread(target=handle, args=(conn,))
    thread.start()

def socket_accept():
    while True:
        conn, address = server.accept()
        print(f"Connection established! | IP {address[0]} | Port {address[1]}")
        client_conn(conn)

def main():
    create_socket()
    socket_accept()

main()
