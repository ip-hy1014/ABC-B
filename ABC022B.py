from collections import Counter
n = int(input())
a = [int(input()) for _ in range(n)]
ans = 0
c = Counter(a)
for i in c.values():
  if i>1:
    ans += i-1
print(ans)