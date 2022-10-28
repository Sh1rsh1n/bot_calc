def sum(x,y):
	return int(x) + int(y)

def sub(x,y):
	return int(x) - int(y)

def mult(x, y):
	return int(x) * int(y)

def div(x, y, i):
	if i == 1:
		return int(x) / int(y)
	if i == 2:
		return int(x) // int(y)
	if i == 3:
		return int(x) % int(y)
