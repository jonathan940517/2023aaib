def gcd(a,b):
	if a == 0:
		return b
	if b == 0:
		return a
	return gcd(b,a%b)
a,b = map(int,input('Enter two integers: ').split())
print()
print(f'The greatest common divisor of {a} and {b} is',gcd(a,b))