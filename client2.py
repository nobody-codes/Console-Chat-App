import socket
import threading
import os

messages = []

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def display_chat():
    os.system('cls')
    for message in messages:
        print(message)

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            #   Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                messages.append(message)
                display_chat()
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break
        
# Sending Messages To Server
def write():
    while True:
        try:
            message = f"{nickname}: {input('Enter message')}"
            client.send(message.encode('ascii'))
        except socket.error as msg:
            print(f"Socket connection error: {str(msg)}")
        
# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()