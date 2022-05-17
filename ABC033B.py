n = int(input())
s,p = [],[]
for _ in range(n):
  a,b = input().split()
  s.append(a)
  p.append(int(b))
sp = sum(p)//2
ans = "atcoder"
for i in range(n):
  if p[i]>sp:
    ans = s[i]
print(ans)