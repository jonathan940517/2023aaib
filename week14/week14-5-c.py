a = input()
for i in range(0,len(a)):
	print(a[i],sep='',end='')
	if i != len(a)-1:
		print('   ',sep='',end='')