"""
問題文
数列 A (A1,A2,A3,…,AN) が与えられます。
正の整数 k の GCD 度を、A1,A2,A3,…,AN のうち k で割り切れるものの数と定義します。
2 以上の整数のうち GCD 度が最大になるものを一つ求めてください。 GCD 度が最大のものが複数ある場合どれを出力しても構いません。
"""

n = int(input())
a = list(map(int, input().split()))

ans = 0
mx = 0

for x in range(2,1001):
  score = 0
  for b in a:
    if b % x == 0:
      score += 1
  if score > mx:
    ans = x
    mx = score

print(ans)