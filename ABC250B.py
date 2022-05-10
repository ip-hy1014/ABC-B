n,a,b = map(int,input().split())
g = []
for _ in range(5):
  for r in range(a):
    g.append(("."*b + "#"*b)*5) #白タイル始まり
  for r in range(a):
    g.append(("#"*b + "."*b)*5) #黒タイル始まり
for r in range(a*n): #縦はa*n行出力する
  print(g[r][:b*n]) #横はb*n列なので[:b*n]でスライスする

"""
制約が 1<=N<=10 なので最初に必要十分なタイルを用意し、必要な分だけ出力する
"""