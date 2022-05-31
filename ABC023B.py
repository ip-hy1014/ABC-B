n = int(input())
s = input()
l = ["b"]
for i in range(1,101):
  if i%3==1:
    x = "a"+l[i-1]+"c"
    l.append(x)
  if i%3==2:
    x = "c"+l[i-1]+"a"
    l.append(x)
  if i%3==0:
    x = "b"+l[i-1]+"b"
    l.append(x)
if s in l:
  print(l.index(s))
else:
  print(-1)