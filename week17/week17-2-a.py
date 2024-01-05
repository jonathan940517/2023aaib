a = input()
ans = 0
try:
	ans = int(a[1])
except:
	ans = a[2]
print(ans)