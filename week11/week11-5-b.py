a,b=map(int,input().split())
if b < a:
	a,b = b,a
for i in range(a,b+1,1):
	if i % 5 == 0:
		print(i)