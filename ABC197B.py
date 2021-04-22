"""
問題文
縦 H 行、横 W 列のマス目があり、いくつかのマスには障害物が置かれています。
上から i
 番目、左から j 番目のマスをマス (i,j) と表すことにします。
H 個の文字列 S1,S2,S3,…,SH が与えられます。
Si の j 文字目はマス (i,j) の状態を表し、# なら障害物が置かれていることを、. なら障害物が置かれていないことを表します。
このマス目上のあるマスからあるマスが見えるとは、2 つのマスが同じ行または列にあり、2 つのマスの間 (2 つのマス自身を含む) に障害物が 1 つも置かれていないことを意味します。
このマス目上のマスであって、マス目 (X,Y) から見えるもの (マス (X,Y) 自身を含む) の数を求めてください。
"""

H, W, X, Y = map(int, input().split())
X -= 1  # 0スタートにしたいので、-1
Y -= 1
grid = []

for _ in range(H):
    s = input()
    grid.append(s)

ans = 1  # (X, Y)自身も含むので、初期値は1

# 上　X-1 ～ 0
for row in reversed(range(X)):
    if grid[row][Y] == "#":
        break
    else:
        ans += 1

# 下 X+1 ～ H-1
for row in range(X + 1, H):
    if grid[row][Y] == "#":
        break
    else:
        ans += 1

# 左 Y-1 ～ 0
for col in reversed(range(Y)):
    if grid[X][col] == "#":
        break
    else:
        ans += 1

# 右 Y+1 ～ W-1
for col in range(Y + 1, W):
    if grid[X][col] == "#":
        break
    else:
        ans += 1

print(ans)

"""
上下左右の四方向、 (X, Y) の隣からスタートして、'#' にぶつかるまで '.' の数を数える．
"""