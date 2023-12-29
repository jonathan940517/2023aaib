a = list(map(int,input().split()))
a.sort()
ans = 0
for i in range(len(a)-1,-1,-1):
	ans = ans * 10 + a[i]
print(ans+1,end='')