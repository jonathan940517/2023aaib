a,b =input().split()
a = int(a)
b = int(b)
if a % b == 0:
	print(a//b,end='')
else:
	print(a//b + 1,end='')