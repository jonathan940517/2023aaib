a = int(input())
ans = int(100)
if a <= 2000:
	print(ans)
else:
	a = a - 2000
	if a % 500 == 0:
		ans = ans + (a//500)*5
	else:
		ans = ans + (a//500+1)*5
	print(ans)
