n = int(input())
a = [list(input()) for _ in range(n)]
for i in range(n):
  for j in range(n):
    if (a[i][j]=="W" and a[j][i]!="L") or (a[i][j]=="L" and a[j][i]!="W") or (a[i][j]=="D" and a[j][i]!="D"):
      print("incorrect")
      exit()
print("correct")