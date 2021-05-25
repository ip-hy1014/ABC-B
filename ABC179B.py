"""
問題文
高橋君は、「サイコロを 2 個振る」という行動を N 回行いました。
i 回目の出目は Di1,Di2 です。
ゾロ目が 3 回以上続けて出たことがあるかどうか判定してください。
より正確には、Di1=Di2 かつ Di+1,1=Di+1,2 かつ Di+2,1=Di+2,2 を満たすような i が少なくとも一つ存在するかどうか判定してください。

出力
ゾロ目が 3 回以上続けて出たことがあるならば Yes、ないならば No を出力せよ。
"""

n = int(input())
c = 0
for i in range(n):
  a,b = map(int, input().split())
  if a == b:
    c += 1
  else:
    c = 0
  if c == 3:
    print("Yes")
    break
if c != 3:
  print("No")
