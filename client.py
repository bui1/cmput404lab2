import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to a webpage using socket
# stolen from vartec https://stackoverflow.com/users/60711/vartec
# From StackOverflow
# From https://stackoverflow.com/a/10600261
s.connect(("www.google.com", 80))
s.sendall(b"GET /\r\n")
print(s.recv(1024))
s.close()
