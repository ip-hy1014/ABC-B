n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = "Yes"
for i in b:
  if i not in a:
    ans = "No"
    print(ans)
    exit()
  a.remove(i)
print(ans)

#別解
from collections import Counter
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ca = Counter(a)
cb = Counter(b)
print("No" if cb-ca else "Yes")
