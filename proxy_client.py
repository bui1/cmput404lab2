import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
payload = b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"

# Connecting to a webpage using socket
# stolen from vartec https://stackoverflow.com/users/60711/vartec
# From StackOverflow
# From https://stackoverflow.com/a/10600261
s.connect(("localhost", 8001))
s.sendall(payload)
print(s.recv(1024))
s.close()
