# coding: utf-8
"""

多进程+select多路复用服务
使用 multiproccess + socket

在主进程中bind端口号
在worker中accept客户端链接并给客户端连接
然后在worker中select socket连接
"""

import socket
import select
import multiprocessing


class Worker(multiprocessing.Process):
    def __init__(self, socket):
        super(Worker, self).__init__()
        self.socket = socket
        self.rlist = [self.socket, ]
        self.wlist = []
        self.rdata = {}
        self.wdata = {}

    def run(self):
        print "开始socket服务"

        while True:
            rl, wl, xl = select.select(self.rlist, self.wlist, [])
            for sock in rl:  # 对返回值rl判断是否有socket进来，如果有连接进来的话sock激活
                if sock == self.socket:  # 代表有新的链接进来了
                    print "有新连接进来了 ", rl
                    conn, addr = sock.accept()
                    self.rlist.append(conn)  # 把新的客户端链接放到监听列表中，继续托管给select去监听
                else:  # 由于客户端连接进来时socket接收客户端连接请求，将客户端连接加入到了监听列表中(rlist)，客户端发送消息的时候这个连接将触发
                    try:
                        print "客户端发送数据了>>", type(sock)
                        data = sock.recv(1024)  # 接收客户端请求
                        if not data:
                            print "什么都没收到，关闭客户端连接..."
                            sock.close()
                            self.rlist.remove(sock)
                            continue
                        print "received data [{0}] from client {1}".format(data.decode(), sock)

                        self.rdata[sock] = data.decode()  # 将接受到的客户端信息保存下来
                        self.wdata[sock] = data.upper()  # 加工成返回消息, 这里相当于处理客户端请求
                        self.wlist.append(sock)  # 客户端请求处理完成后将客户端socket 添加到wlist中，供后续发送数据
                    except:
                        sock.close()
                        self.rlist.remove(sock)

            for sock in wl:  # 当有可写事件发生的时候，代表可以给客户端返回数据，
                print "当有可写事件发生的时候，", wl
                sock.send(self.wdata[sock])  # 将要返回的数据放到sock中，
                # 发送完从可写列表中移除 socket，避免重复发送
                self.wlist.remove(sock)
                self.wdata.pop(sock)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 8800))  # 绑定端口号和地址

    server.listen(5)  # 最大接收5 个socket请求
    server.setblocking(False)  # 设置为非阻塞IO
    for _ in range(multiprocessing.cpu_count()):
        p = Worker(server)
        p.start()


if __name__ == '__main__':
    start_server()



