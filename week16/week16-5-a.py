a = int(input())
ans = a ** 0.5
if ans % 1 != 0:
	print('0',end='')
else:
	print(int(ans),end='')