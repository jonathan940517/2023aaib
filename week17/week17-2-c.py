a = int(input())
h = a // 3600
m = a % 3600 // 60
s = a % 60
if h < 10:
	h = '0'+ str(h)
if m < 10:
	m = '0'+ str(m)
if s < 10:
	s = '0'+ str(s)
print(f'{h}:{m}:{s}',end='')