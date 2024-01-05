a = int(input())
temp = 1
while a>0:
	print(a%10*temp,'',end='')
	temp = temp * 10
	a = a // 10