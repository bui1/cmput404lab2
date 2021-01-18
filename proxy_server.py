import socket

# Stolen from https://docs.python.org/3/library/socket.html#example
# Python3 socket docs to listen to connections and print data afterwards
HOST = 'www.google.com'
PORT = 80
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    connection, addr = s.accept()

    with connection:
        print('Connected by', addr)
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.sendall(data)
