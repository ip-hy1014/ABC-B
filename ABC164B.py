from operator import indexOf


#何回攻撃すれば0以下になるか考察
import math
a,b,c,d = map(int, input().split())
print("Yes" if math.ceil(a/d) >= math.ceil(c/b) else "No")

#別解
a,b,c,d = map(int, input().split())
while True:
    c -= b
    if c <= 0:
        print("Yes")
        exit()
    a -= d
    if a <= 0:
        print("No")
        exit()

#別解2
a,b,c,d = map(int, input().split())
for _ in range(101):
  c -= b
  if c <= 0:
    print("Yes")
    break
  a -= d
  if a <= 0:
    print("No")
    break