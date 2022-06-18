n = int(input())
a = list(map(int,input().split()))
ans = 0
c = 0
for i in a[::-1]:
  c+=i
  if c>=4:
    ans += 1
print(ans)


#別解
n = int(input())
a = list(map(int,input().split()))
ans = 0
masu = [0]*4
for x in a:
  masu2 = [0]*4
  masu[0] = 1
  for i in range(4):
    if masu[i]==1:
      if i+x>=4:
        ans += 1
      else:
        masu2[i+x]=1
  masu = masu2
print(ans)