a = input()
ans = 0
for i in range(len(a)):
	try:
		b = int(a[i])
		ans += 1
	except:
		continue
print(ans)