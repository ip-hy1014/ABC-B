n,m = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
cd = [list(map(int,input().split())) for _ in range(m)]
for i in range(n):
  e = 10**19
  for j in range(m):
    md = abs(ab[i][0]-cd[j][0])+abs(ab[i][1]-cd[j][1])
    if e>md:
      e = md
      ans = j+1
  print(ans)