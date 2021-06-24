s = input()
ans = 0
c = 0
for i in range(len(s)):
  if s[i] in "ACGT":
    c += 1
  else:
    c = 0
  ans = max(c,ans)
print(ans)