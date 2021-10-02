s = list(input())
t = list(input())
for i in range(len(s)):
  if s[i]!=t[i]:
    s[i],s[i+1] = s[i+1],s[i]
    break
if s == t:
  print("Yes")
else:
  print("No")