s = []
for i in range(3):
  s.append(input())
l = ["ABC","ARC","AGC","AHC"]
ans = list(set(s)^set(l))
print(ans[0])

#別解
s = []
for i in range(3):
  s.append(input())
l = ["ABC","ARC","AGC","AHC"]
ans = set(s)^set(l)
print(*ans)
