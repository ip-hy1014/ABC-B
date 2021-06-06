n = int(input())
ans = False
for i in range(1,10):
  for j in range(1,10):
    if i * j == n:
      ans = True
if ans:
  print("Yes")
else:
  print("No")

#別解
n = int(input())
q = [i*j for i in range(1,10) for j in range(1,10)]
if n in q:
  print("Yes")
else:
  print("No")