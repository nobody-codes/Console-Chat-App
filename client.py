'''
import socket
import sys
import threading

messages = []

def create_socket():
    try:
        global user_name
        global host
        global port
        global client
        
        user_name = input("Choose your User Name: ")
        
        client = socket.socket()
        host = '192.168.1.10'
        port = 9999
    except socket.error as msg:
        print(f"Socket creation error: {str(msg)}")
    
def connect_socket():
    try:
        global host
        global port
        global client
        
        client.connect((host, port))
        print(f"Connection has been established! | HOST {host}  | Port {port}")
        client_handle(client)
    except socket.error as msg:
        print(f"Socket Connection error: {str(msg)}")
        
def display_chat():
    for message in messages:
        print(message, end='\n')
        
# Listening to Server
def receive(client):
    while True:
        try:
            # Receive Message From Server
            message = client.recv(1024).decode('ascii')
            
            # Response to Server's User name Request
            if message == 'SUN': 
                client.send(user_name.encode('ascii'))
            else:
                messages.append(messages)
                display_chat()
                #print(message)
        except socket.error as msg:
            print(f"Socket Connection error: {str(msg)}")
            client.close()
            break
        
# Sending Messages To Server
def write(client):
    while True:
        message = f"{user_name}: {input('Type message: ')}"
        messages.append(messages)
        display_chat()
        client.send(message.encode('ascii'))
    
def client_handle(client):
    # Starting Threads For Listening And Writing
    receive_thread = threading.Thread(target=receive, args=(client,))
    receive_thread.start()

    write_thread = threading.Thread(target=write, args=(client,))
    write_thread.start()


def main():
    create_socket()
    connect_socket()
    
main()
'''


import socket
import threading
import sys
import os 

messages = []

def create_socket():
    try:
        global user_name
        global client
        user_name = input("Choose your User Name: ")
        
        client = socket.socket()
        host = '127.0.0.1'
        port = 9999
        client.connect((host, port))
        print(f"Connection has been established! | HOST {host} | PORT {port}")
    except socket.error as msg:
        print(f"Socket creation error: {str(msg)}")
        sys.exit()

def display_chat():
    os.system('cls')
    for message in messages:
        print(message)

# Listening to Server
def receive(client):
    while True:
        try:
            # Receive Message From Server
            message = client.recv(1024).decode('ascii')
            
            # Respond to Server's User Name Request
            if message == 'SUN': 
                client.send(user_name.encode('ascii'))
            else:
                messages.append(message)  # Append only the received message
                display_chat() # Display the new message
        except socket.error as msg:
            print(f"Socket connection error: {str(msg)}")
            client.close()
            break

# Sending Messages To Server
def write(client):
    while True:
        try:
            message = f"{user_name}: {input('Type message: ')}"
            messages.append(message)  # Append the user's message
            print(message)  # Display the new message locally
            client.send(message.encode('ascii'))
        except socket.error as msg:
            print(f"Socket send error: {str(msg)}")
            client.close()
            break

def client_handle(client):
    # Starting Threads For Listening And Writing
    receive_thread = threading.Thread(target=receive, args=(client,))
    receive_thread.start()

    write_thread = threading.Thread(target=write, args=(client,))
    write_thread.start()

def main():
    create_socket()
    client_handle(client)

main()