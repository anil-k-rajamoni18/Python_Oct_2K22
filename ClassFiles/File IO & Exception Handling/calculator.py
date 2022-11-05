def add(a,b):
	''' will return the addition of two numbers'''
	c = a+b 
	print("sum is ",c)

def greet(name):
	''' it will greet the user '''
	return f"Hello, Hi {name}"


def maxOfList(lst):
	''' return the max element of a LIST '''
	return max(lst)

def fac(n):
	f = 1
	for i in range(1,n+1):
		f = f*i
	return f