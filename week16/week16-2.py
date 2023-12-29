for i in range(a-1,-1,-1):
	for j in range(i):
		print(' ',end='')
	for k in range(1+(a-1-i)*2):
		print('*',end='')
	print()