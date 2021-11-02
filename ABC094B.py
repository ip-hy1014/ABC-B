n,m,x = map(int,input().split())
a = list(map(int,input().split()))
b = x
c = x
ans1 = 0
ans2 = 0
for _ in range(b,n+1):
  b += 1
  if b in a:
    ans1 += 1
for _ in range(c,0,-1):
  c -= 1
  if c in a:
    ans2 += 1
print(min(ans1,ans2))