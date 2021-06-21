n = int(input())
x = [[input().split(), i+1] for i in range(n)]
x = sorted(x, key=lambda x:(x[0][0], -int(x[0][1])))
for i in range(n):
  print(x[i][1])