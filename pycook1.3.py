# coding: utf8

from collections import deque 

"""
读取文件的过程中保留最后几个有限的历史元素
"""

def save_history_iterms(iterm, num=4):
	save_list = deque(maxlen=num)
	save_list.append(iterm)
	yield save_list


for i in xrange(10):
	print save_history_iterms(i)



	


