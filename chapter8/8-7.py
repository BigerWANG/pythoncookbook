# coding: utf-8

"""
在子类中调用父类的一个已经被覆盖的方法

"""

class Person:
	def __init__(self):
		self.x = 0


class Chinese:
	def __init__(self):
		super().__init__()
		self.y = 1

