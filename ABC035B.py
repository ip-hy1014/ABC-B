s = input()
t = int(input())
x,y,c = 0,0,0
for i in s:
  if i=="L":
    x -= 1
  if i=="R":
    x += 1
  if i=="U":
    y -= 1
  if i=="D":
    y += 1
  if i=="?":
    c += 1
d = abs(x)+abs(y)
if t==1:
  print(d+c)
else:
  ans = d-c
  if ans<0: #行きすぎた場合は偶奇分け→？の出現回数が奇数なら原点から1遠ざかるし、偶数なら行って来いで0になる
    ans %= 2
  print(ans)