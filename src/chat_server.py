"""
Based on: https://www.geeksforgeeks.org/simple-chat-room-using-python/
Try: python chat_server.py <IP address> 8081
"""

import socket
import select
import sys

from _thread import *

import logging as log
import sanitizer

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
    """
    Receives messages from client, evaluates them, checks for invalid chars and broadcasts if valid.
    """
    msg = "The server says hello!\n".encode()  # 'send' commands expect bytes-like, so encode/decode
    conn.send(msg)  # print message for sender

    while True:
        # print('Client Loop')  # print to server
        try:
            message = conn.recv(2048)
            print(sanitizer.sanitizer(message))

            if message:
                # print(addr)
                message = f"{addr[0]}: {str(message.decode())}"
                message = message.strip().encode()
                broadcast(message, conn)  # send message to server and receiver
            else:
                remove(conn)
        except Exception as e:
            print(e)
            if type(e).__name__ == 'RuntimeError':
                conn.send(str(e).encode())
            continue


def broadcast(message, connection):
    """
    Broadcoasts message to users.
    """
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
    """
    Removes a client connection.
    """
    print('Removing: ', connection)
    if connection in list_of_clients:
        list_of_clients.remove(connection)


# Main Server Loop
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
