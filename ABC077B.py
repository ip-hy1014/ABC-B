import math
n = int(input())
while n>0:
  if math.sqrt(n).is_integer():
    print(n)
    exit()
  else:
    n-=1