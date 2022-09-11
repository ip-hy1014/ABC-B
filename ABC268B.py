s = input()
t = input()
ls = len(s)
lt = len(t)
if ls>lt:
  print("No")
else:
  for i in range(len(s)):
    if s[i]!=t[i]:
      print("No")
      exit()
  print("Yes")

#別解
s = input()
t = input()
print("Yes" if t.startswith(s) else "No")