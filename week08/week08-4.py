a=[3,0,1,8,7,2,5,4,6,9]
for i in range(1,len(a)):
  if a[i] < a[i-1]:
    a[i], a[i-1] = a[i-1], a[i]
    #沒想到python swap那麼簡單
print(a)