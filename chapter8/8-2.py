# coding: utf-8

"""
自定义字符串的格式化


"""

class  Date(object):
	"""docstring for  Date"""
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day
		self._fmt = {
		"ymd": "{d.year}-{d.month}-{d.day}",
		"dmy": "{d.day}-{d.month}-{d.year}",
		"mdy": "{d.month}-{d.day}-{d.year}",
		}

	def __format__(self, code):
		"""
		定义一个__format__方法，接收一个自定义参数，在该方法中实现自定义函数
		"""
		if not code:
			code = "ymd"

		return self._fmt[code].format(d=self)



d = Date(year="2018", day="18", month="9")
print format(d)
print format(d, "dmy")

		

