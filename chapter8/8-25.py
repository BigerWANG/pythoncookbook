# coding: utf-8

"""
创建缓存实例
在创建一个对象时，如果之前使用同样的参数创建过这个对象，则返回它的缓存引用
"""
import weakref
	


class Spam(object):
	"""docstring for Spam"""
	def __init__(self, name):
		self.name = name



_spam_cache = weakref.WeakValueDictionary()

def get_spam(name):

	if name not in _spam_cache:
		s = Spam(name)
		_spam_cache[name] = s
	else:
		s = _spam_cache[name]
	return s


a = get_spam("foo")
b = get_spam("bar")
c = get_spam("foo")


print a == b

print a == c

print id(a)
print id(b)
print id(c)


