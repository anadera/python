def me(words):
  count = 0
  for x in words:
    if len(x) > 2 and x[0] == x[-1]:
      count = count + 1
  return count

def fx(words):
  a = []
  b = []
  xlist = []
  for x in words:
    if x[0] == 'x':
      a.append(x)
    else:
      b.append(x)
  a.sort()
  b.sort()
  xlist.extend(a)
  xlist.extend(b)
  return xlist

def fsort(list):
  return list.sort(key=lambda fx: fx[1])

c = ['aca', 'dad', 'mom', 'rrr', 'tuc', 'toot', 'ii']
d = 'aca, ara, arra, acc'
print(me(c), me(d))

e = ['tix', 'xyz', 'apple', 'xacadu', 'aabbbccc']
print(fx(e))

f = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
fsort(f)
print (f)
