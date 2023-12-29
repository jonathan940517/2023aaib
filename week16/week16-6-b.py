a = list(map(int,input().split()))
ans = 1000000
rk = 0
for i in range(len(a)):
	if a[i] < ans:
		rk = i+1
		ans = a[i]
print(rk,int(1.2 * 3600 / ans))