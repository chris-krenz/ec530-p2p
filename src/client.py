"""
Based on: https://www.geeksforgeeks.org/simple-chat-room-using-python/
Try: python client.py <IP address> 8081
"""

import socket
import select
import sys

import logging as log

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print("Try: python client.py <IP address> 8081")  # Get IP on Mac: ifconfig; Win: ipconfig
    exit()

IP_address = str(sys.argv[1])
Port       = int(sys.argv[2])

server.connect((IP_address, Port))

# Main Client Loop
while True:
    sockets_list        = [sys.stdin, server]
    read_sockets, _, __ = select.select(sockets_list, [], [])

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            if message:
                print(message.decode())
        else:
            message = sys.stdin.readline()
            server.send(message.encode())  # 'send' commands expect bytes-like, so encode/decode

server.close()
