n = int(input())
s = set()
ans = 0
while True:
  ans += 1 #インデックスを出力
  if n in s:
    print(ans) #重複する要素が出現したらbreak
    break
  s.add(n) #要素を追加していく
  if n%2==0:
    n=n//2
  else:
    n=3*n+1