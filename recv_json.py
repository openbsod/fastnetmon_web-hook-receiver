#!/usr/bin/python
# -*- coding: utf-8 -*-


import socket
import json
import simplejson
import struct

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '188.143.202.200'
port = 8088

buffer_size = 4096

serverSocket.bind((host, port))
serverSocket.listen(10)

while True:
    clientSocket, address = serverSocket.accept()
    data = clientSocket.recv(buffer_size)
    jdata = data[data.index("{"):]

    print(jdata)
