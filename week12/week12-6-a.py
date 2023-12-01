a = int(input())
ans = int(0)
for i in range(1,a,1):
	ans = ans + i * (i + 1)
print(ans)