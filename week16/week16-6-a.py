a = int(input())
ans = 0
for i in range(1,a+1):
	ans += i + i * 10
print(ans,end='')