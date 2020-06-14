# coding: utf-8

import heapq
"""
用py实现一个优先级队列, 每次pop都返回优先级最高的那个元素
"""

class PriorityQueue(object):
	"""用py实现一个优先级队列, 每次pop都返回优先级最高的那个元素"""
	def __init__(self):
		self._queue = list()
		self._index = 0

	def push(self, iterm, priority):
		# 优先级，元素的原始索引， 元素值， 按照数字越大优先级越大的规则
		heapq.heappush(self._queue, (-priority,  self._index, iterm)) 
		self._index += 1

	def pop(self):
		return heapq.heappop(self._queue)[-1]  





class  Iterm(object):
	"""docstring for  Iterm"""
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "< name: %s >" % self.name

		

def main():
	p = PriorityQueue()
	p.push(Iterm("foo"), 0)
	p.push(Iterm("foo1"), 1)
	p.push(Iterm("foo2"), 2)
	p.push(Iterm("foo3"), 3)
	p.push(Iterm("foo4"), 4)
	p.push(Iterm("foo5"), 5)
	p.push(Iterm("foo6"), 6)

	print p.pop()
	print p.pop()
	print p.pop()


if __name__ == '__main__':
	main()
