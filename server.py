import socket
import sys
import time


# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global server
        host = ""
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


# Establish connection with a client (socket must be listening)
def socket_accept():
    try:
        conn, address = server.accept()
        print(f"Connection has been established! | IP {address[0]} | Port {str(address[1])}")
        start_chat(conn) # start chat with client
        conn.close()
    except socket.error as msg:
        print(f"Socket Accecpting error {str(msg)} \n Retrying...")
        socket_accept()

# Send messages to client or a friend
def start_chat(conn):
    while True:
        message = input("Type message: ")
        try:
            conn.send(str.encode("server: " + message))
            if message == 'quit':
                # time.sleep(2)
                conn.close()
                server.close()
                break
            else:
                client_response = str(conn.recv(1024),"utf-8")
                if client_response == 'client: quit':
                    print("client: Ended Chat")
                    conn.close()
                    server.close()
                    break
                else:
                    print(client_response, end="\n")
        except socket.error as msg:
            print(f"Sever Chat error : {msg}")


def main():
    create_socket()
    bind_socket()
    socket_accept()

while True:
    main()