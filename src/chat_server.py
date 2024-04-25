"""
Based on: https://www.geeksforgeeks.org/simple-chat-room-using-python/
"""

import socket
import select
import sys

from _thread import *

import logging as log

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    print("Try: python chat_server.py <IP address> 8081")  # Get IP on Mac: ifconfig; Win: ipconfig
    exit()

IP_address = str(sys.argv[1])
Port       = int(sys.argv[2])

server.bind((IP_address, Port))

server.listen(100)

list_of_clients = []


def clientthread(conn, addr):

    msg = "The server says hello!\n".encode()  # 'send' commands expect bytes-like, so encode/decode
    conn.send(msg)

    while True:
        # print('Client Loop')
        try:
            message = conn.recv(2048)
            if message:
                # print(addr)
                message = f"{addr[0]}: {str(message.decode())}"
                message = message.strip().encode()
                broadcast(message, conn)
            else:
                remove(conn)
        except:
            print('Exception!')
            continue


def broadcast(message, connection):
    # print('Broadcasting!')
    for client in list_of_clients:
        if client != connection:
            try:
                client.send(message)
                print('Broadcast to: ', client, '\n', message.decode())
            except:
                print('Broadcast except!')
                client.close()
                remove(client)


def remove(connection):
    print('Removing: ', connection)
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    print('Starting Server...')
    conn, addr = server.accept()
    # conn.setblocking(False)

    list_of_clients.append(conn)
    # print('List of clients: ', list_of_clients)

    print(f"{addr[0]} connected!")
    start_new_thread(clientthread, (conn, addr))


conn.close()
server.close()
