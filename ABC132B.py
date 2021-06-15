n = int(input())
p = list(map(int,input().split()))
ans = 0
for i in range(n-2):
  if p[i] < p[i+1] < p[i+2]:
    ans += 1
  elif p[i] > p[i+1] > p[i+2]:
    ans += 1
print(ans)

#別解
n = int(input())
p = list(map(int,input().split()))
ans = 0
for i in range(n-2):
  a = p[i:i+3]
  a.sort()
  if p[i+1] == a[1]:
    ans += 1
print(ans)
