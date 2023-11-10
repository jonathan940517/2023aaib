a = input().split()
for i in range(len(a)):
	a[i] = int(a[i])
for i in range(len(a)):
	for j in range(1,len(a)):
		if a[j-1]>a[j]:
			a[j],a[j-1]=a[j-1],a[j]
for i in range(len(a)):
	print(a[i])