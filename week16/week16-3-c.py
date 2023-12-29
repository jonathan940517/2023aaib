a = list(map(int,input().split()))
ans = int(0)
for i in range(len(a)):
	if i == 0:
		ans = ans + a[i] * 50
	elif i == 1:
		ans = ans + a[i] * 5
	else:
		ans = ans + a[i]
print(ans,end='')