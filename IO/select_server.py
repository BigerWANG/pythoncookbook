# coding: utf-8

"""
IO多路复用之select
"""

from socket import AF_INET, SOCK_STREAM, socket
import select


server = socket(AF_INET, SOCK_STREAM)
server.bind(("127.0.0.1", 8800))

server.listen(5)  # 最大接收5 个socket请求
server.setblocking(False)  # 设置为非阻塞IO

rlist = [server, ]  # 加入select监听列表

rdata = {}  # 存放客户端返回的数据

wlist = []
wdata = {}

print "开始监听。"
count = 0

while True:
    rl, wl, xl = select.select(rlist, wlist, [])
    for sock in rl:  # 对返回值rl判断是否有sock进来，如果有连接进来的话sock激活
        if sock == server:
            conn, addr = sock.accept()
            rlist.append(conn)  # 把新的客户端链接放到监听列表中，继续托管给select去监听
        else:  # 由于客户端连接进来时socket接收客户端连接请求，将客户端连接加入到了监听列表中(rlist)，客户端发送消息的时候这个连接将触发
            try:
                data = sock.recv(1024)
                if not data:
                    sock.close()
                    rlist.remove(sock)
                    continue
                print "received {0} from client {1}".format(data.decode(), sock)

                rdata[sock] = data.decode()  # 将接受到的客户端信息保存下来
                wdata[sock] = data.upper()  # 加工成返回消息 并添加到wlist中
                wlist.append(sock)
            except:
                sock.close()
                rlist.remove(sock)

    for sock in wl:  # 当有可写事件发生的时候
        sock.send(wdata[sock])
        wlist.remove(sock)
        wdata.pop(sock)











