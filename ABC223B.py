s = input()
l = [s]
for _ in range(len(s)-1):
  s = "".join(s[1:]+s[0])
  l.append(s)
print(min(l))
print(max(l))