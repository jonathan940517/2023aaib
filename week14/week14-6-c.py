a,b,c = input().split()
a = int(a)
c = int(c)
if b == '+':
	print(a+c,end='')
elif b == '-':
	print(a-c,end='')
elif b == '*':
	print(a*c,end='')
else:
	print(a//c,end='')