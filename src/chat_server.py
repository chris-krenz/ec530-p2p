"""
https://www.geeksforgeeks.org/simple-chat-room-using-python/
"""

import socket
import select
import sys

from _thread import *

import logging as log

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    log.info("Correct usage: script, IP address, port number")
    exit()

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.bind((IP_address, Port))
server.listen(100)
list_of_clients = []


def clientthread(conn, addr):

    msg = "Hello!".encode()

    conn.send(msg)

    while True:
        try:
            message = conn.recv(2048)
            if message:
                log.info("<" + addr[0] + "> " + message)
                message_to_send = "<" + addr[0] + "> " + message
                broadcast(message_to_send, conn)
            else:
                remove(conn)
        except:
            continue


def broadcast(message, connection):
    for client in list_of_clients:
        if client != connection:
            try:
                client.send(message.encode())
            except:
                client.close()
                remove(client)


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    conn, addr = server.accept()
    conn.setblocking(False)
    list_of_clients.append(conn)
    log.info(addr[0] + " connected")
    start_new_thread(clientthread, (conn, addr))

conn.close()
server.close()
