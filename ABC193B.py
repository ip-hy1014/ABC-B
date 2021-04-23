"""
問題文
高橋くんは人気ゲーム機「スヌケマシン」を買おうとしています。
スヌケマシンを販売している店は店 1,2,…,N の N 軒あり、店 i は高橋くんの現在地から徒歩 Ai 分、
スヌケマシンの販売価格は Pi 円、現在のスヌケマシンの在庫は Xi 台です。
高橋くんは今から徒歩でスヌケマシンを販売している店に向かい、店に着いたときにスヌケマシンの在庫があればスヌケマシンを買います。
しかし、スヌケマシンは人気商品なので、今から 0.5,1.5,2.5,… 分後に全ての店でスヌケマシンの在庫が (存在するなら) 1 台減ります。
高橋くんがスヌケマシンを買うことができるか判定し、できる場合は買うのに必要な最小の金額を求めてください。
できない場合は、-1 を出力せよ。
"""

n = int(input())
inf = float("inf")
ans = inf
for i in range(n):
  a, p, x = map(int, input().split())
  if x - a > 0:
    ans = min(ans, p)
if ans == inf:
  print(-1)
else:
  print(ans)

#公式解答
INF = 1 << 30
N = int(input())
ans = INF
for i in range(N):
    A, P, X = map(int, input().split())
    if X > A and ans > P:
        ans = P
if ans == INF:
    ans = -1
print(ans)
