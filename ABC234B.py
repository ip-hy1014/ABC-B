n = int(input())
xy = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for x1,y1 in xy:
  for x2,y2 in xy:
    ans = max(ans,(x1-x2)**2+(y1-y2)**2)
print(ans**0.5)

# 別解
import math
n = int(input())
x = [0]*n
y = [0]*n
for i in range(n):
  x[i],y[i] = map(int,input().split())
ans = 0
for i in range(n):
  for j in range(i+1,n):
    X = x[i]-x[j]
    Y = y[i]-y[j]
    ans = max(ans,math.sqrt(X*X+Y*Y))
print(ans)
