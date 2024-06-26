import socket

import logging as log

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello client!")
    data = s.recv(1024)

log.info(f"Received {data!r}")
