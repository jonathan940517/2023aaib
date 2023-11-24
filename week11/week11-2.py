a,b = map(int,input().split())
a=abs(a)
b=abs(b)
for i in range(min(a,b),0,-1):
  if a % i == 0 and b % i == 0:
    print(i,end='')
    break