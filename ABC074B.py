n = int(input())
k = int(input())
x = list(map(int,input().split()))
ans = 0
for i in x:
  ans += 2*min(abs(i),abs(i-k))
print(ans)

#別解
n = int(input())
k = int(input())
x = list(map(int,input().split()))
ans = 0
for i in range(n):
  if x[i]<k-x[i]:
    ans += x[i]*2
  else:
    ans += (k-x[i])*2
print(ans)