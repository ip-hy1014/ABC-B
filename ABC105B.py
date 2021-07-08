n = int(input())
for i in range(25):
  for j in range(15):
    if 4*i + 7*j == n:
      print("Yes")
      exit()
print("No")