"""
問題文
縦 H マス、横 W マスのマス目があります。上から i 行目、左から j 列目のマスには、ブロックが Aij 個あります。
どのマスにも同じ個数のブロックがある状態にするには、最小で何個のブロックを取り除けばよいでしょうか？
"""

#各要素から最小値を引いたものの和を計算
import numpy as np
h,w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
a = np.array(a)
print(np.sum(a-np.min(a)))

#ブロックの総和からmin*h*wを引く
h,w = map(int, input().split())
s = 0
a_min = 1000
for _ in range(h):
  a = [*map(int, input().split())]
  s += sum(a)
  a_min = min(a_min,min(a))
ans = s-a_min*h*w
print(ans)