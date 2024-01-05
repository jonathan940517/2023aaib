a = input()
for i in range(len(a)):
	if i!= 0 and (len(a)-i) % 3 == 0:
		print(',',end='')
	print(a[i],end='')