# coding: utf-8

"""
多进程+select多路复用服务
使用 socketserver

"""
import select
import SocketServer
import traceback


class Server(SocketServer.BaseRequestHandler):

    def handle(self):
        self.rlist = [self.request, ]  # 加入select监听列表
        self.rdata = {}  # 存放客户端返回的数据

        self.wlist = []
        self.wdata = {}
        print "New connection: ", self.client_address
        rl, wl, xl = select.select(self.rlist, self.wlist, [])
        for sock in rl:  # 对返回值rl判断是否有socket进来，如果有连接进来的话sock激活
            print "客户端发送数据了>>", type(sock)
            data = sock.recv(1024)  # 接收客户端请求
            if not data:
                print "什么都没收到，关闭客户端连接..."
                sock.close()
                self.rlist.remove(sock)
                continue
            print "received data [{0}] from client {1}".format(data.decode(), sock)
            self.rlist.append(sock)
            self.rdata[sock] = data.decode()  # 将接受到的客户端信息保存下来
            self.wdata[sock] = data.upper()  # 加工成返回消息, 这里相当于处理客户端请求
            self.wlist.append(sock)  # 客户端请求处理完成后将客户端socket 添加到wlist中，供后续发送数据
            print self.wlist
        for sock in wl:  # 当有可写事件发生的时候，代表可以给客户端返回数据，
            print "当有可写事件发生的时候，", wl
            sock.send(self.wdata[sock])  # 将要返回的数据放到sock中，
            # 发送完从可写列表中移除 socket，避免重复发送
            self.wlist.remove(sock)
            self.wdata.pop(sock)


def start_server():

    # 这里是主进程
    addr = ("127.0.0.1", 8888)
    server = SocketServer.ForkingTCPServer(addr, Server)
    print "启动 多进程 socket server ...", addr
    server.serve_forever()


if __name__ == '__main__':
    start_server()






