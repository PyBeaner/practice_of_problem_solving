def test1():
	l = []
	for i in range(1000):
		l = l+[i]

def test2():
	l = []
	for i in range(1000):
		l.append(i)

def test3():
	l = [i for i in range(1000)]

def test4():
	l = list(range(1000))

if __name__ == '__main__':
	from timeit import Timer
	t1 = Timer('test1()', "from __main__ import test1")
	t2 = Timer('test2()', "from __main__ import test2")
	t3 = Timer('test3()', "from __main__ import test3")
	t4 = Timer('test4()', "from __main__ import test4")
	print 'concat', t1.timeit(10)
	print 'append', t2.timeit(10)
	print 'comprehension',t3.timeit(10)
	print 'list range', t4.timeit(10)