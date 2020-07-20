# coding: utf-8

"""
多进程+select多路复用服务

"""

from multiprocessing import Process
from socket import AF_INET, SOCK_STREAM, socket
import select


server = socket(AF_INET, SOCK_STREAM)
server.bind(("127.0.0.1", 8800))   # 绑定端口号和地址

server.listen(5)  # 监听传入连接，等于5表示内核已经接到了连接请求，但服务器还没有调用accept进行处理的连接个数最大为5，这个值不能无限大，因为要在内核中维护连接队列
server.setblocking(False)  # 设置为非阻塞IO

rlist = [server, ]  # 加入select监听列表

rdata = {}  # 存放客户端返回的数据

wlist = []
wdata = {}

print "开始监听。"
count = 0

while True:
    rl, wl, xl = select.select(rlist, wlist, [])
    for sock in rl:  # 对返回值rl判断是否有socket进来，如果有连接进来的话sock激活
        if sock == server:  # 代表有新的链接进来了
            print "有新链接进来了 ", rl
            conn, addr = sock.accept()  # 表示接受连接并返回连接的地址和一个新的套接字对象conn，可以用来接收和发送数据
            rlist.append(conn)  # 把新的客户端链接放到监听列表中，继续托管给select去监听
        else:  # 由于客户端连接进来时socket接收客户端连接请求，将客户端连接加入到了监听列表中(rlist)，客户端发送消息的时候这个连接将触发
            try:
                print "客户端发送数据了>>", type(sock)
                data = sock.recv(1024)  # 接收客户端请求数据
                if not data:
                    sock.close()
                    rlist.remove(sock)
                    continue
                print "received data [{0}] from client {1}".format(data.decode(), sock)
                rdata[sock] = data.decode()  # 将接受到的客户端信息保存下来
                wdata[sock] = data.upper()  # 加工成返回消息 并添加到wlist中
                wlist.append(sock)
            except:
                sock.close()
                rlist.remove(sock)

    for sock in wl:  # 当有可写事件发生的时候，代表可以给客户端返回数据，
        print "当有可写事件发生的时候，", wl
        sock.send(wdata[sock])  # 将要返回的数据放到sock中，
        # 发送完从可写列表中移除 socket，避免重复发送
        wlist.remove(sock)
        wdata.pop(sock)
        sock.close()










