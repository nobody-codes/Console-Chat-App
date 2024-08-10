import socket
import sys
client = socket.socket()
host = '192.168.1.10'
port = 9999

client.connect((host, port))

while True:
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
            