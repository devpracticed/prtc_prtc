
x = 1000

def foo(x):
	def bar(y):
		print(x + y)
	return bar

b1 = foo(10)
b2 = foo(20)

print(b1)

print('------\n')

print(b2(30))
