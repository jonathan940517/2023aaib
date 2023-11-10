a = input().split()
ans = int(0)
for i in range(1,len(a)):
	a[i] = int(a[i])
	ans = ans + a[i]
print(ans)