x,y = map(int, input().split())
if 2*x<=y<=4*x and y % 2 == 0:
  print("Yes")
else:
  print("No")

#別解
x,y = map(int, input().split())
for i in range(x+1):
  if 2*i + 4*(x-i) == y:
    print("Yes")
    exit()
print("No")