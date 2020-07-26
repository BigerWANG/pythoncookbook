# coding: utf-8

from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM




client = socket(AF_INET, SOCK_STREAM)
client.connect(("127.0.0.1", 8800))


while True:
    msg = raw_input(">>>: ", )
    if not msg:
        break
    client.send(msg.encode("utf-8"))
    data = client.recv(1024)
    print data.decode('utf-8')

client.close()





