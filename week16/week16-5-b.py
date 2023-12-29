a,b = map(int,input().split())
ans = 0
flag = False
for i in range(a,b+1):
	for k in range(2,i):
		if i % k == 0:
			flag = True
			break
	if flag == False:
		ans += 1
	flag = False
print(ans)