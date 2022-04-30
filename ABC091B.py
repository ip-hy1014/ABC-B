from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]
ans = [0]
sc = Counter(s)
tc = Counter(t)
for key,value in sc.items():
  ans.append(value-tc[key])
print(max(ans))