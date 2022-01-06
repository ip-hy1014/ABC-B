n = int(input())
a = list(map(int,input().split()))
ans = 0
mx = 0
for i in range(2,1001):
  c = 0
  for j in a:
    if j%i==0:
      c+=1
  if c>mx:
    ans = i
    mx = c
print(ans)
