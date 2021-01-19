#!/usr/bin/env python3
import socket
from multiprocessing import Process


def thread(client_connection, client_addr):
    client_request = client_connection.recv(1024)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('www.google.com', 80))
    s.sendall(client_request)

    while True:
        data_from_server = s.recv(1024)
        if (len(data_from_server) > 0):
            # send response back to client after contacting webserver
            client_connection.sendall(data_from_server)
        else:
            break

    s.close()
    client_connection.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('localhost', 8001))
s.listen(2)

while True:
    client_connection, client_address = s.accept()
    client_connection.settimeout(60)

    p = Process(target=thread, args=(client_connection, client_address))
    p.daemon = True
    p.start()
