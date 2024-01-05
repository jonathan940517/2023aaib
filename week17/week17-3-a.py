a = int(input())
ans = 1
k = 1
while a >= k:
	ans += 1
	k += ans
print(ans,end='')