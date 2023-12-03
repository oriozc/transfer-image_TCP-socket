import socket


def send_file(socket):
    file = open("img.png", "rb")
    data = file.read(1024)
    while data:
        socket.send(data)
        data = file.read(1024)


print("client is running")
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "127.0.0.1"
PORT = 2000

my_socket.connect((HOST, PORT))

send_file(my_socket)

my_socket.close()