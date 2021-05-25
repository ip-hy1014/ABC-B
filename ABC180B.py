"""
問題文
N 次元空間内の点 (x1,…,xN) が与えられます。
原点からこの点までの、マンハッタン距離、ユークリッド距離、チェビシェフ距離をそれぞれ求めてください。 ただし、それぞれの距離は次のように計算されます。
マンハッタン距離： |x1|+…+|xN|
ユークリッド距離： √|x1|^2+…+|xN|^2
チェビシェフ距離： max(|x1|,…,|xN|)
"""

import math

n = int(input())
x = list(map(int, input().split()))

a = 0

for i in x:
  a += abs(i)**2
a = math.sqrt(a)

print(sum([abs(i) for i in x]))
print(a)
print(max([abs(i) for i in x]))

#別解
import math

n = int(input())
x = list(map(abs, map(int, input().split()))) #最初に絶対値でリスト化
x_2 = [i**2 for i in x]

print(sum(x))
print(math.sqrt(sum(x_2)))
print(max(x))