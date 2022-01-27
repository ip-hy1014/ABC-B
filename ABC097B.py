n = int(input())
ans = 1
for i in range(1,n):
  for j in range(2,n):
    c = i**j
    if c>n:
      break
    ans = max(ans,c)
print(ans)