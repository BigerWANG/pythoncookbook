# coding: utf-8

"""
import select 导入select模块

epoll = select.epoll() 创建一个epoll对象

epoll.register(文件句柄,事件类型) 注册要监控的文件句柄和事件

事件类型:

　　select.EPOLLIN    可读事件

　　select.EPOLLOUT   可写事件

　　select.EPOLLERR   错误事件

　　select.EPOLLHUP   客户端断开事件

epoll.unregister(文件句柄)   销毁文件句柄

epoll.poll(timeout)  当文件句柄发生变化，则会以列表的形式主动报告给用户进程,timeout

                     为超时时间，默认为-1，即一直等待直到文件句柄发生变化，如果指定为1

                     那么epoll每1秒汇报一次当前文件句柄的变化情况，如果无变化则返回空

epoll.fileno() 返回epoll的控制文件描述符(Return the epoll control file descriptor)

epoll.modfiy(fineno,event) fineno为文件描述符 event为事件类型  作用是修改文件描述符所对应的事件

epoll.fromfd(fileno) 从1个指定的文件描述符创建1个epoll对象

epoll.close()   关闭epoll对象的控制文件描述符

"""


