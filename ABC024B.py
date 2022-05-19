n,t = map(int,input().split())
ans = 0
a = [int(input()) for _ in range(n)]
for i in range(n-1):
  if a[i+1]-a[i]<t:
    ans += a[i+1]-a[i]
  else:
    ans += t
print(ans+t)