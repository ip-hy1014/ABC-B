#お菓子を持っているすぬけ君のリストを作成して重複分を削除，Nからその数を引いたものが答え
n,k = map(int, input().split())
l = []
for i in range(k):
  d = int(input())
  a = list(map(int, input().split()))
  l += a
s = set(l)
sl = len(s)
print(n-sl)

#別解
import itertools
from collections import Counter
n,k = map(int,input().split())
l = []
for i in range(k):
  d = int(input())
  a = list(map(int,input().split()))
  l.append(a)
l = list(itertools.chain.from_iterable(l))
c = Counter(l)
ans = 0
r = []
for j in c.keys():
  r.append(j)
print(n-len(r))
