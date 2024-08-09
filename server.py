import socket
import sys


# Create a Socket ( connect two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


# Establish connection with a client (socket must be listening)

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established! |" + " IP " + address[0] + " | Port" + str(address[1]))
    start_chat(conn) # start chat with client
    conn.close()

# Send commands to client/victim or a friend
def start_chat(conn):
    while True:
        cmd = input("Type message : ")
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode("server : " + cmd))
            try:
                client_response = str(conn.recv(1024),"utf-8")
                print(client_response, end="")
            except socket.error as msg:
                print(msg)


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()