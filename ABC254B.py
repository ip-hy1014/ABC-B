n = int(input())
a = [[1]*(i+1) for i in range(n)]
for i in range(n-1):
  for j in range(1,i+1):
    a[i+1][j] = a[i][j]+a[i][j-1]
for i in a:
  print(*i)