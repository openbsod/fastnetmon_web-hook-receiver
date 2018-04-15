#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import json
import struct

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '10.10.202.200'
port = 8088

buffer_size = 4096

serverSocket.bind((host, port))
serverSocket.listen(10)

while True:
    clientSocket, address = serverSocket.accept()
    data = clientSocket.recv(buffer_size).decode("utf-8")
    jdata = data.encode("utf-8")[data.index("{"):]

    print(jdata)
