
def b(x):
	try:
		assert x<5
		return 100
	except:
		print("test")

def a():
	for i in range(10):
		n = b(i)
		print(n," ",i)
		print("nnnn")

a()