#2k-1個が黒で塗られている可能性がある
k,x = map(int, input().split())
ans = x-k #一番左の座標は x-k+1で表せる
for _ in range(2*k-1):
  ans += 1
  print(ans,end=" ")