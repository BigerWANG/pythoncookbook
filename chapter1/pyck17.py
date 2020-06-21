# coding: utf-8


from collections import defaultdict, OrderedDict

def main():
	# dd = defaultdict(list)
	# dd["1"].append(1)
	# dd["1"].append(1)
	# dd["1"].append(1)
	# dd["1"].append(1)

	# print dd["1"]

	d = OrderedDict()
	d["1"] = 1
	d["2"] = 2
	d["3"] = 3
	d["4"] = 4
	d["5"] = 5
	for k, v in d.iterms():
		print k, v
		
if __name__ == '__main__':
	main()