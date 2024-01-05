a = input().split()
for i in range(len(a)):
	a[i]=int(a[i])
a.sort()
print(f'[{a[0]},{a[-1]}]',end='')