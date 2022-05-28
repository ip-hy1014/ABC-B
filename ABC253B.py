h,w = map(int,input().split())
s = [input() for _ in range(h)]
l = []
m = []
for i in range(h):
  for j in range(w):
    if s[i][j] == "o":
      l.append(i)
      m.append(j)
x = abs(l[0]-l[1])
y = abs(m[0]-m[1])
print(x+y)