import socket
# Make a file called echo_server.py that listens for incoming connections and echos any received data

# Stolen from https://docs.python.org/3/library/socket.html#example
# Python3 socket docs to listen to connections and print data afterwards
HOST = 'localhost'
PORT = 8001
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
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
