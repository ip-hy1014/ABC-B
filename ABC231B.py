from collections import Counter
n = int(input())
s = []
for i in range(n):
  s.append(input())
c = Counter(s)
print(c.most_common()[0][0])