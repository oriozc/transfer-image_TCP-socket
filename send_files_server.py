import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def recive_file(socket):
    file = open("copy_img.png", "wb")
    chunk = socket.recv(1024)
    while chunk:
        file.write(chunk)
        chunk = socket.recv(1024)


HOST = "127.0.0.1"
PORT = 2000

server_socket.bind((HOST, PORT))

server_socket.listen(3)
print("server is listening")
client_socket, client_addr = server_socket.accept()
print(client_addr)
print("accepted new connection")

recive_file(client_socket)

server_socket.close()