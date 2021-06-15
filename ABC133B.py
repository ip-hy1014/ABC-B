n,d = map(int,input().split())
x = [list(map(int,input().split())) for _ in range(n)]
ans = 0
for i in range(n):
  for j in range(i+1,n):
    a = 0
    for y,z in zip(x[i],x[j]):
      a += (y-z)**2
    if a**0.5 == int(a**0.5):
      ans += 1
print(ans)