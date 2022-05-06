n,m = map(int,input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]
for i in range(n-m+1): #画像Bが画像Aが含まれてるか調べるには全部で(n-m+1)*(n-m+1)パターンあり、全探索する
  for j in range(n-m+1):
    ok = True
    for k in range(m):
      for l in range(m):
        if a[i+k][j+l] != b[k][l]:#各パターンを見ていき、一致しない箇所があったらFalse
          ok = False
    if ok:
      print("Yes")
      exit()
print("No")