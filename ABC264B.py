#中央のマスからの距離が奇数なら黒、偶数なら白
#r行目c列目のマスが黒になるのはそのマスと中央のマスからのチェビシェフ距離がmax(abs(r-8),abs(c-8))奇数のとき
r,c = map(int,input().split())
if max(abs(r-8),abs(c-8))%2 == 1:
  print("black")
else:
  print("white")