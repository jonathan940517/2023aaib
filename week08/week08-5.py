a=[3,0,1,8,7,2,5,4,6,9]
for i in range(len(a)):
  for j in range(1,len(a)):
    if a[j]<a[j-1]:
      temp = a[j]
      a[j] = a[j-1]
      a[j-1] = temp
  print(a)