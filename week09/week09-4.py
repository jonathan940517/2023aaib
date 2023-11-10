a = list(map(int,input().split()))
ans = a[0]
for i in a:
    if i > ans :
      ans = i
print('最大值:',ans)

for i in a:
  print(i)