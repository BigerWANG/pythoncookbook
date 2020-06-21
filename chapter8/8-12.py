# coding: utf-8

"""
定义接口或抽象基类

定义一个抽象类，并通过执行类型检查来确保子类实现了某些特定方法
"""
from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
	"""
	抽象类的特点是不能被直接实例化，
	"""
	@abstractmethod
	def read(self, maxbytes=-1):
		pass

	@abstractmethod
	def write(self, data):
		pass


class SocketStream(IStream):
	"""	抽象类的目的是是让别的类继承它并实现特定的方法"""
	def read(self, maxbytes=-1):
		pass

	def write(self, data):
		pass

	