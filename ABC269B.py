s = [input() for _ in range(10)]
a = 1<<60
b = 1>>60
c = 1<<60
d = 1>>60
for i in range(10):
  for j in range(10):
    if s[i][j]=="#":
      a = min(a,i+1)
      b = max(b,i+1)
      c = min(c,j+1)
      d = max(d,j+1)
print(a,b)
print(c,d)