a = 12345 #int(input())
ans = int(0)
while a > 0:
    ans = ans * 10 + a % 10
    print('a=',a,'a%10=',a%10,'ans=',ans)
    a = a // 10
print('ans=',ans)