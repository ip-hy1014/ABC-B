n = int(input())
p = list(map(int,input().split()))
ans = 0
c = n
while c!=1:
  ans += 1
  c = p[c-2]
print(ans)