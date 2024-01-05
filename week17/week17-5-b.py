a = input().split()
for i in range(len(a)):
	a[i] = int(a[i])
x1 = a[0]
x2 = a[2]
y1 = a[1]
y2 = a[3]
print(abs(x1-x2)*abs(y1-y2),end='')