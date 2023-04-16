n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
b = [list(map(int,input().split())) for _ in range(n)]

def rot(a, b):
  for i in range(n):
      for j in range(n):
          if a[i][j]==1 and b[i][j]!=1:
              return False
  return True
for _ in range(4):
  a = [a for a in zip(*a[::-1])]
  if rot(a,b):
    print("Yes")
    exit()
print("No")