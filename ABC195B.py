"""
問題文
みかんがたくさんあります。どのみかんの重さも A グラム以上 B グラム以下であることがわかっています。（みかんの重さは整数とは限りません。）
この中からいくつかのみかんを選んだところ、選んだみかんの重さの合計がちょうど W キログラムになりました。
選んだみかんの個数として考えられる最小値と最大値を求めてください。ただし、このようなことが起こり得ないなら、かわりにそのことを報告してください。

出力
選んだみかんの個数としてありえる最小値と最大値を空白区切りでこの順に出力せよ。ただし、与えられた条件に合うような個数が存在しない場合、かわりに UNSATISFIABLE と出力せよ。
"""

A, B, _W = map(int, input().split())
W = 1000*_W #単位を揃える
mn = float("inf")
mx = -1
for n in range(1, 10**6+1): #Wの最大値は10^6g(100万g)なので，みかんの数は10^6個まで試す
  l = A*n
  r = B*n
  if l <= W <= r: #AN≤W≤BN であれば，みかん N 個で W キログラムを作ることができる
    mn = min(mn, n)
    mx = max(mx, n)
if mx == -1:
  print("UNSATISFIABLE")
else:
  print(mn, mx)

#公式解答
import math

a,b,w=map(int,input().split())
upper=int(math.floor(1000*w/a))
lower=int(math.ceil(1000*w/b))

if lower>upper:
  print("UNSATISFIABLE")
else:
  print(lower,upper)

