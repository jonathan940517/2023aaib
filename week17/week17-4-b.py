a = int(input())
ans = int(0)
for i in range (1,a+1):
	if a % i == 0:
		ans = ans + i
print(ans,end='') 