"""
問題文
xy 平面上に 1,2,…,N の番号が付けられた N 個の点があります。
点 i は (xi,yi) にあり、N 個の点の x 座標は互いに異なります。
以下の条件を満たす整数の組 (i,j) (i<j) の個数を求めてください。
点 i と点 j を通る直線の傾きが −1 以上 1 以下である。
"""

n = int(input())
ans = 0
xy = []
for _ in range(n):
  xy.append(list(map(int, input().split())))
for i in range(n):
  for j in range(i):
    if -1 <= (xy[i][1]-xy[j][1])/(xy[i][0]-xy[j][0]) <= 1:
      ans += 1
print(ans)

#別解
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
a = 0
for i in range(n):
  for j in range(i):
    if -1 <= (l[i][1]-l[j][1])/(l[i][0]-l[j][0]) <= 1:
      a += 1
print(a)