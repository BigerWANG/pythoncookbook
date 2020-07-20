# coding: utf-8

from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM




class Clinet(Thread):
    def __init__(self, msg):
        super(Clinet, self).__init__()
        self.msg = msg
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(("127.0.0.1", 8800))

    def run(self):
        if not self.msg:
            return
        self.client.send(self.msg.encode("utf-8"))
        data = self.client.recv(1024)
        print data.decode('utf-8')
        self.client.close()


def main():
    s = "a"
    for i in s:
        msg = "hahahaha{}".format(i)
        c = Clinet(msg)
        c.start()
        c.join()


if __name__ == '__main__':
    main()





