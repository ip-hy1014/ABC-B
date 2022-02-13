a = [list(input().split())[::-1] for _ in range(4)]
for i in a[::-1]:
  print(*i,sep=" ")