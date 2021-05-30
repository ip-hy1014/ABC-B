#TLE
from functools import partial, reduce
from operator import indexOf, mul
n = int(input())
a = list(map(int, input().split()))
ans = reduce(mul,a)
if ans > 10**18:
  print(-1)
else:
  print(ans)

#関数使うやつ
def main():
  N = int(input())
  A = list(map(int, input().split()))

  if 0 in A:
    print(0)
    return

  ans = 1
  for a in A:
    ans *= a
    if ans > 10**18:
      print(-1)
      return

  print(ans)

main()

#別解
n = int(input())
a = list(map(int, input().split()))

ans = 1
if 0 in a:
  print(0)
else:
  for i in a:
    ans *= i
    if ans > 10**18:
      ans = -1
      break
  print(ans)