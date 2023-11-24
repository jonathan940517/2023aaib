def gcd(a,b):
 # print(a,b)
  if a==0: return b
  if b==0: return a
  return gcd(b, a%b)


a,b = map(int,input().split())
a=abs(a)
b=abs(b)
ans = gcd(a,b)
print(ans,end='')