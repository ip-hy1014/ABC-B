n,x = map(int, input().split())
l = list(map(int, input().split()))
d = 0
ans = 1 #座標0で跳ねるため確実に1回は跳ねる
for i in l:
  d += i
  if d<=x:
    ans += 1
print(ans)