# coding: utf-8

"""
IO多路复用之select
"""

from socket import AF_INET, SOCK_STREAM, socket
import select


def select_server():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(("127.0.0.1", 8800))   # 绑定端口号和地址

    server.listen(5)  # 最大接收5 个socket请求
    # server.setblocking(False)  # 设置为非阻塞IO

    rlist = [server, ]  # 加入select监听列表

    rdata = {}  # 存放客户端返回的数据

    wlist = []
    wdata = {}

    print "开始socket服务"

    while True:
        rl, wl, xl = select.select(rlist, wlist, [])
        for sock in rl:  # 对返回值rl判断是否有socket进来，如果有连接进来的话sock激活
            if sock == server:  # 代表有新的链接进来了
                print "有新连接进来了 ", rl
                conn, addr = sock.accept()
                rlist.append(conn)  # 把新的客户端链接放到监听列表中，继续托管给select去监听
            else:  # 由于客户端连接进来时socket接收客户端连接请求，将客户端连接加入到了监听列表中(rlist)，客户端发送消息的时候这个连接将触发
                try:
                    print "客户端发送数据了>>", type(sock)
                    data = sock.recv(1024)  # 接收客户端请求
                    if not data:
                        print "什么都没收到，关闭客户端连接..."
                        sock.close()
                        rlist.remove(sock)
                        continue
                    print "received data [{0}] from client {1}".format(data.decode(), sock)

                    rdata[sock] = data.decode()  # 将接受到的客户端信息保存下来
                    wdata[sock] = data.upper()  # 加工成返回消息, 这里相当于处理客户端请求
                    wlist.append(sock)  # 客户端请求处理完成后将客户端socket 添加到wlist中，供后续发送数据
                except:
                    sock.close()
                    rlist.remove(sock)

        for sock in wl:  # 当有可写事件发生的时候，代表可以给客户端返回数据，
            print "当有可写事件发生的时候，", wl
            sock.send(wdata[sock])  # 将要返回的数据放到sock中，
            # 发送完从可写列表中移除 socket，避免重复发送
            wlist.remove(sock)
            wdata.pop(sock)


if __name__ == '__main__':
    select_server()





