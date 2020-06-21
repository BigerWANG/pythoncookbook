# coding: utf-8

"""
让对象支持上下文管理协议（使用with语句）

为了让对象兼容with语句，需要实现__enter__()和__exit__()方法
__enter__()是with语句入口，返回的实例对象self，既是 as 语句定义的变量
__exit__()负责with语句收尾工作，关闭资源，接收异常信息并进行处理等
"""

from socket import socket, AF_INET, SOCK_STREAM
from functools import partial
import traceback


class LazyConnection(object):
	"""使用上下文管理器创建一个网络连接"""
	def __init__(self, addr, family=AF_INET, type=SOCK_STREAM):
		self.addr = addr
		self.family = family
		self.type = type
		self.socket = None


	def __enter__(self):
		if self.socket:
			raise RuntimeError("Already connected")
		self.socket = socket(self.family, self.type)
		self.socket.connect(self.addr)
		return self.socket

	def __exit__(self, exc_ty, exc_val, tb): # 接收三个参数，异常类型，异常值，追溯信息
		# if exc_ty:
		# 	self.socket.close()
		# 	self.socket = None
		# 	raise exc_ty(exc_val, traceback.print_tb(tb)) # 使用traceback 标准库返回错误栈
		print "exec .. "
		self.socket.close()
		self.socket = None
		print "exit .. "
		return True

class  LasyConnectionPool(object):
	"""docstring for  LasyConnectionPool"""
	def __init__(self, addr, family=AF_INET, type=SOCK_STREAM):
		self.addr = addr
		self.family = family
		self.type = type
		self.connections = []


	def __enter__(self):
		if self.socket:
			raise RuntimeError("Already connected")
		socket = socket(self.family, self.type)
		socket.connect(self.addr)
		self.connections.append(socket) # 每生成一个新连接加入到队列中，可以限制长度
		return socket

	def __exit__(self, exc_ty, exc_val, tb): # 接收三个参数，异常类型，异常值，追溯信息
		# if exc_ty:
		# 	self.socket.close()
		# 	self.socket = None
		# 	raise exc_ty(exc_val, traceback.print_tb(tb)) # 使用traceback 标准库返回错误栈
		print "exec .. "
		self.connections.pop().close()
		print "exit .. "
		return True
		

lasy_conn = LazyConnection(('www.python.org', 80))
with lasy_conn as conn:
	conn.send(b"GET /index.html HTTP/1.0\r\n")
	raise RuntimeError("is a error")
	conn.send(b"Host: www.python.org\r\n")
	conn.send(b'\r\n')
	resp  = b"".join(iter(partial(conn.recv, 8192), b""))
	print resp



		