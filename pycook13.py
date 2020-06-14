# coding: utf8

from collections import deque 

"""
读取文件的过程中保留最后几个有限的历史元素
"""

def save_history_iterms(iterms, num=4):
	save_list = deque(maxlen=num)
	for i in iterms:
		save_list.append(i)
		yield save_list
		




if __name__ == '__main__':
	g = save_history_iterms(range(10), 4)
	
