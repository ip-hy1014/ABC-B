""""
問題文
あなたは今、高さ 1000 の非常に高いタワーの下にいます。
タワーから距離 D 離れた位置の上空 H の高さに UFO がおり（入出力例 1 の図を参照してください）、あなたは UFO に電波を届けたいです。
タワーと UFO の間には遮蔽物が N 個あります。
i 番目の遮蔽物はタワーから UFO の方向に向かって距離 di の場所に位置していて、高さは hi です。
あなたはタワーを上って、あなたと UFO の間の直線上に遮蔽物が 1 つも無い状態にしたいです。上る必要のある最低の高さを求めてください。
なお、地面は凹凸のない水平面であり、タワー及び遮蔽物は地面と垂直に建っているものとします。
また、あなたと UFO の間の直線上にちょうど遮蔽物の上端があるとき、その遮蔽物には遮蔽されていないものとします。
"""

N,D,H = map(int, input().split())
ans = 0.0
for i in range(N):
  d,h = map(int, input().split())
  a = (H-h)/(D-d)
  b = H-D*a
  if ans < b:
    ans = b
print(ans)


#公式解答
N, D, H = map(int, input().split())
ans = 0.0
for i in range(N):
    d, h = map(int, input().split())
    h -= d * (H - h) / (D - d)
    if ans < h:
        ans = h
print(ans)
