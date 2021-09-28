n,x = map(int,input().split())
l = []
for i in range(n):
  m = int(input())
  l.append(m)
l.sort()
sl = sum(l)
a = x-sl
b = a//l[0]
ans = n+b
print(ans)