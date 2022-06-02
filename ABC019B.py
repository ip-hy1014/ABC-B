s = input()
ans = ""
c = 1
f = s[0]
for i in range(1,len(s)):
  t = s[i]
  if f!=t:
    ans += f+str(c)
    f = t
    c = 1
  else:
    c += 1
ans += f+str(c)
print(ans)