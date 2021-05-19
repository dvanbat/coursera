m = '3141592653589793238462643383279502884197169399375105820974944592'
n = '2718281828459045235360287471352662497757247093699959574966967627'
# m = '31415926535897932384626433832795'
# n = '27182818284590452353602874713526'
# m = '3141592653589793'
# n = '2718281828459045'
# m = 3141592653589793238462643383279502884197169399375105820974944592
# n = 2718281828459045235360287471352662497757247093699959574966967627
# m = '12345678'
# n = '87654321'
# m = '1234'
# n = '4321'

def Karatsuba(x, y, level):
	''' ax + b cx + d
	acx^2 + (ad + bc)x + db
	(a + b)(c + d) - ac - bd
	result = Karatsuba(a, b) '''

	if x == '0': x = '00'
	if y == '0': y = '00'
	le = level

	a = str()
	b = str()
	c = str()
	d = str()
	l = int(len(x) / 2)
	a = int(x[:l])
	b = int(x[l:])
	c = int(y[:l])
	d = int(y[l:])
	x10 = int('1' + '0'*l)

	if len(x) % 2 == 1 or len(y) % 2 == 1:
		return int(x)*int(y)
	if l < 2:
		e1 = a * c
		e2 = b * d
		e3 = (a + b) * (c + d) - e1- e2
		result = e1 * x10 ** 2 + e3 * x10 + e2
	else:
		e1 = Karatsuba(str(a), str(c), le + 1)
		e2 = Karatsuba(str(b), str(d), le + 1)
		e3 = Karatsuba(str(a + b), str(c + d), le + 1) - e1 - e2
		result = e1 * x10 ** 2 + e3 * x10 + e2

	return(result)


print(Karatsuba(m, n, 1))
print(int(m)*int(n))