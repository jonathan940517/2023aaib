a = int(input())
temp = a
b = int(0)
while a>0:
	b = b * 10 + a % 10
	a = a // 10
print(f'{temp}+{b}={temp+b}')