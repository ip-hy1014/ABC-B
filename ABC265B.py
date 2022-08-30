n,m,t = map(int,input().split())
a = list(map(int,input().split()))
b = [0]*n
for _ in range(m):
  x,y = list(map(int,input().split()))
  b[x-1] = y
for i in range(n-1):
  if t - a[i]<=0:
    print("No")
    exit()
  t -= a[i]
  t += b[i+1]
print("Yes")