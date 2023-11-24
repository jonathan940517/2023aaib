a = list(map(int,input().split()))
ans = int(0)
for i in range(len(a)):
	if a[i]%3==0:
		ans = ans + 1
print(ans)