# coding: utf-8

"""

有一个字典列表，需要根据某几个字典字段来排序这个列表
"""
from operator import itemgetter, attrgetter

def sorted_iterm():
	rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
	]
	rows_by_fname = sorted(rows, key=itemgetter("fname"))  # 以此方法排序比使用lambda速度要快一些
	print rows_by_fname
	row_by_uid = sorted(rows, key=lambda x : x["uid"])
	print row_by_uid



class User:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "<User {}>".format(self.name)


def sorted_obj():
	user_list = [User(10), User(9), User(8), User(7), User(6)]
	print user_list
	s = sorted(user_list, key=lambda i: i.name)
	s = sorted(user_list, key=attrgetter("name"))
	print s


def main():
	sorted_iterm()
	sorted_obj()
if __name__ == '__main__':
	main()
