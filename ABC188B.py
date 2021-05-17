"""
問題文
2 つの N 次元ベクトル A=(A1,A2,A3,…,AN),B=(B1,B2,B3,…,BN) が与えられます。
A と B の内積が 0 かどうかを判定してください。
すなわち、A1B1+A2B2+A3B3+⋯+ANBN=0 かどうかを判定してください。

出力
A と B の内積が 0 ならば Yes を、0 でないならば No を出力せよ。
"""

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
  ans += a[i]*b[i]
print("Yes" if ans==0 else "No")
