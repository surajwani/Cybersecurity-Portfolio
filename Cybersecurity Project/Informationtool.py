import sys
import socket

target = sys.argv[1]
print("IPV4 Address:",  socket.gethostbyname(target))