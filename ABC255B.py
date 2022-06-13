"""
全ての人について、その人から最も近い『明かりを持った人』までの距離の最大値が答え
"""
n,k = map(int,input().split())
a = list(map(int,input().split()))
xy = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
  mx = 10**18
  for j in range(k):
    x1,y1 = xy[i] #調べる人
    x2,y2 = xy[a[j]-1] #明かりを持った人
    mx = min(mx,(x1-x2)**2 + (y1-y2)**2) #調べる人から明かりを持った人までの距離の最大値
  ans = max(ans,mx)
print(ans**0.5)