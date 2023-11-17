a = list(map(int,input().split()))
for i in range (len(a)):
	for j in range(1,len(a)):
		if a[j] < a[j-1]:
			a[j-1],a[j] = a[j],a[j-1]
count = int(0)
for i in a:
	print(f' {i}',end='')
	count = count + 1
	if count % 10 == 0 and count != 100:
		print()