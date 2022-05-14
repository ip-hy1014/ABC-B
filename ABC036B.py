import numpy as np
n = int(input())
s = [list(input()) for _ in range(n)]
ans = np.rot90(s,3)
for i in range(n):
  print("".join(ans[i]))