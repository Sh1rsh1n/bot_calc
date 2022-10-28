
def cal_compl(real_1, imag_1, real_2, imag_2, action):
	a = complex(int(real_1), int(imag_1))
	b = complex(int(real_2), int(imag_2))

	if action == "+":
		return a + b
	elif action == "-":
		return a - b
	elif action == "*":
		return a * b
	elif action == "/" and b != 0:
		return a / b

