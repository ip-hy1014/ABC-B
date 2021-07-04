#PyPyじゃないとTLEする
p = int(input())
c = [1,2,6,24,120,720,5040,40320,362880,3628800]
dp = [987654321] * 1001
dp[0] = 0
for i in range(p+1):
  for j in c:
    if i-j >= 0:
      dp[i] = min(dp[i-j]+1, dp[i])
print(dp[i])

#貪欲法
from math import factorial

p = int(input())
answer = 0
for i in range(10, 0, -1):
  while factorial(i) <= p:
    answer += 1
    p -= factorial(i)
print(answer)
