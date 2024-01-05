flag = False
ans = int(0)
while(True):
	a = input().split()
	for i in range (len(a)):
		a[i] = int(a[i])
		if a[i] > 0:
			ans = ans + a[i]
		if a[i] == 0:
			flag = True
			break
	if flag == True:
		break
print(ans,end='')
	