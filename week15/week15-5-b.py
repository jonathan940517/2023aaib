a = input()
b = input()
if len(a) > len(b):
	print('1',end='')
if len(a) < len(b):
	print('-1',end='')
if len(a) == len(b):
	print('0',end='')