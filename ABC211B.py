a = input()
b = input()
c = input()
d = input()
l = ["3B", "HR", "2B", "H"]
e = []
e.append(a)
e.append(b)
e.append(c)
e.append(d)
l.sort()
e.sort()
if l==e:
  print("Yes")
else:
  print("No")

#別解
s = [input() for _ in range(4)]
l = []
l = set(s)
if len(l) == 4:
  print("Yes")
else:
  print('No')