a = input()
if a.isalpha() == True:
	if a.islower() == True:
		print('L',end='')
	else:
		print('U',end='')
elif a.isdigit() == True:
	print('D',end='')
else:
	print('O',end='')