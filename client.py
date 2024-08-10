import socket
import sys

def create_socket():
    try:
        global host
        global port
        global client
        
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
        start_chat(client)
    except socket.error as msg:
        print(f"Socket Connection error: {str(msg)}")
    
def start_chat(client):
    while True:
        try:
            server_response = client.recv(1024).decode("utf-8")
            if server_response == 'server: quit':
                print("Sever: Ended Chat")
                client.close()
                break
            else:
                print(server_response)
                send_msg = input("Type message: ")
                client.send(str.encode("client: "+send_msg))
                if send_msg == 'quit':
                    print("client: Ended Chat")
                    client.close()
                    break
        except socket.error as msg:
            print(f"Chat Communication error : {str(msg)}")


def main():
    create_socket()
    connect_socket()
    
main()