n,m = map(int,input().split())
c = [0]*(n+1)
for _ in range(m):
  a,b = map(int,input().split())
  c[a] += 1
  c[b] += 1
for i in range(1,n+1):
  print(c[i])