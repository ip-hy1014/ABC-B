"""
問題文
高橋君のスマートフォンのバッテリー容量は N [mAh] であり、時刻 0.5,1.5,2.5,… に、つまり時刻 n+0.5(n は整数) を迎える度にバッテリー残量が 1 [mAh] ずつ減少します。
高橋君はスマートフォンを満充電した状態で時刻 0 に外出し、途中で M 回カフェを訪れ、時刻 T に帰宅します。
i 回目に訪れるカフェには時刻 Ai から時刻 Bi まで滞在します。
カフェに滞在している間はスマートフォンを充電するため、バッテリー残量は減少せず、代わりに時刻 n+0.5(n は整数) を迎える度に 1 [mAh] ずつ増加します。
ただし既にバッテリー残量がバッテリー容量と等しい場合、バッテリー残量は増えも減りもしません。
高橋君が途中でスマートフォンのバッテリー残量が 0 になることなく帰宅することができるかを判定してください。

出力
高橋君が途中でスマートフォンのバッテリー残量が 0 になることなく帰宅することができるなら Yes を、できないなら No を出力せよ。
"""

n,m,t = map(int, input().split())

power = n
now = 0

for _ in range(m):
  a,b = map(int, input().split())
  power -= a - now
  if power <= 0:
    print("No")
    exit()
  else:
    power += b-a
    if power > n:
      power = n
    now = b
power -= t - now
if power <= 0:
  print("No")
else:
  print("Yes")

N,M,T=map(int,input().split())
Battery=N
Jikoku=0
for i in range(M):
  A,B=map(int,input().split())
  Battery-=A-Jikoku
  if Battery<=0:
    print('No')
    exit()
  else:
    Battery+=B-A
    if Battery>N:
      Battery=N
    Jikoku=B
Battery-=T-Jikoku
if Battery<=0:
  print('No')
else:
  print('Yes')
