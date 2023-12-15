n = input('Enter the number of values to be processed: ').split()
ans = int(1)
for i in range(1,len(n),1):
	print('Enter a value: ',end='')
	a = int(n[i])
	ans = ans * a
print('Product of the',len(n)-1,'values is',ans,end='')