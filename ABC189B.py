"""
問題文
高橋君はお酒を N 杯飲みました。
i 番目に飲んだお酒は、量が Vi ml、アルコール度数が Pi % です。
高橋君はアルコールの摂取量が X ml を超えると酔っ払います。
高橋君が酔っ払ったのは何杯目のお酒を飲んでいるときですか。ただし、N 杯全てのお酒を飲んだあとでも酔っ払っていない場合は、かわりに -1 を出力してください。
"""

n,x = map(int, input().split())
ans = 0
for i in range(n):
  v,p = map(int, input().split())
  ans += v*p
  if ans > 100*x:
    print(i+1)
    exit()

print(-1)