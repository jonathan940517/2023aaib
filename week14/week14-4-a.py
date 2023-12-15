a = int(input())
ans = int(100)
a -= 1500
if a > 0:
	if a % 250 ==0:
		ans = ans + (a // 250) * 5
	else:
		ans = ans + ((a // 250)+1) * 5
print(ans,end='')