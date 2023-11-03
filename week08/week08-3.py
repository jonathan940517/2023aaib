a = [1,3,5,7,9,11,13,15,17]
for i in range(1,len(a)):
  print(f'a[{i}]={a[i]},a[{i-1}]={a[i-1]}')
  if a[i] - a[i-1] == a[0] - a[1]:
    print("失敗")
print("檢查成功")