s = input()
t = input()
ans = 0

for s_1,t_1 in zip(s,t):
  if s_1 != t_1:
    ans += 1

print(ans)