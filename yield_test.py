# coding: utf-8


def foo():
	print "start...."
	while True:
		res = yield 4
		print "res: ", res

def main():
	g = foo()
	print g.next()
	print "***"*10
	print g.next()


if __name__ == '__main__':
	main()