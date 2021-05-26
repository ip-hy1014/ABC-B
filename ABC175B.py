n = int(input())
l = sorted(list(map(int, input().split())))
ans = 0
#三角形の成立条件 i+j>k

for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      if l[i] != l[j] != l[k] and l[i] + l[j] > l[k]:
        ans += 1
print(ans)

#別解
from itertools import *
n = int(input())
a = sorted(list(map(int,input().split())))
ans = 0
for i,j,k in combinations(a,3): #ソートされた順で重複なし
    if i<j<k and i+j>k:
      ans += 1
print(ans)