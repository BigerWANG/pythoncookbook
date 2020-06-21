# coding: utf-8

import heapq
import random
"""
查找最大或最小的N个元素
"""

def main():
	print dir(heapq)
	l = range(10, 20)
	random.shuffl(l)
	print heapq.nlargest(3, l)

if __name__ == '__main__':
	main()

