n = int(input())
s = list(map(int,input().split()))
ans = 0
for i in s:
  ok = False
  for a in range(1,1001):
    for b in range(1,1001):
      if 4*a*b+3*a+3*b==i:
        ok = True
  if not ok:
    ans += 1
print(ans)