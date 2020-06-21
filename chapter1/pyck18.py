# coding: utf-8

"""
怎样在字典中进行计算操作（最小值，最大值，排序）
"""


def main():
	prices = {
	    'ACME': 45.23,
	    'AAPL': 612.78,
	    'IBM': 205.55,
	    'HPQ': 37.20,
	    'FB': 10.75
	} 

	# 1，使用zip将字典的kv反转过来，然后进行最大值最小值的判断

	iterms = zip(prices.values(), prices.keys())

	print max(iterms)

	print min(iterms)

	print sorted(iterms)

if __name__ == '__main__':
	main()