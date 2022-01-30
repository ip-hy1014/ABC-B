import numpy as np
h,w = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(h)]
b = np.transpose(a)
for i in b:
  print(*i)