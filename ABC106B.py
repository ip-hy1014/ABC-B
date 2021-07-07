n = int(input())
ans = 0
for i in range(1,n+1,2):
  l = 0
  for j in range(1,n+1):
    if i % j == 0:
      l += 1
  if l == 8:
    ans += 1
print(ans)