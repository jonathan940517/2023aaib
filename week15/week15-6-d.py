a = list(map(int,input().split()))
a.pop()
ans = 0
for i in a:
	if i > 0:
		ans+=1
print(ans,end='')