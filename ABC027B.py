n = int(input())
a = list(map(int,input().split()))
ans = 0
s = sum(a)//n
if sum(a)!=s*n:
  print(-1)
else:
  for i in range(n-1):
    if a[i]!=s:
      ans += 1
      a[i+1] += a[i]-s
  print(ans)