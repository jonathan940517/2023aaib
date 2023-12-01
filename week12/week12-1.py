def gcd(a,b):
  if a == 0:
    return b
  if b == 0:
    return a
  return gcd(b,a%b)

a,b = map(int,input().split())
ans = gcd(a,b)
print(f'a/b={a//ans}/{b//ans}')