s = 'qaafjkahgkl'
d = {}
for i in s:
  if i in d:
    d[i] = d[i] + 1
  else:
    d[i] = 1
  print('char=',i,'dict=', d)