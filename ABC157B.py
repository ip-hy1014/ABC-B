a = [list(map(int, input().split())) for _ in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]

for i in range(3):
  for j in range(3):
    if a[i][j] in b:
      a[i][j]=0 #ビンゴカードに書かれている数字と一致するものがあったら 0 にする

#縦横のビンゴ判定
for i in range(3):
  if a[i][0]+a[i][1]+a[i][2]==0 or a[0][i]+a[1][i]+a[2][i]==0:
    print('Yes')
    exit()

#斜めのビンゴ判定
if a[0][0]+a[1][1]+a[2][2]==0 or a[0][2]+a[1][1]+a[2][0]==0:
    print('Yes')
    exit()

print('No')