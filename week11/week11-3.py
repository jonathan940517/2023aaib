def gcd(a,b):
  print(a,b)
  if a==0: return b
  if b==0: return a
  return gcd(b, a%b)

a = 98765432101
b = 123456789012
ans = gcd(a,b)
print(ans)