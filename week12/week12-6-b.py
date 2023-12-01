a,b = map(int,input().split())
sum = int(0)
for i in range(a,b+1):
	if i%3==0:
		sum = sum+i
print(sum,end='')