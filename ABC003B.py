s = input()
t = input()
l = ['a','t','c','o','d','e','r']
ans = "You can win"
for i in range(len(s)):
  if s[i]!=t[i]:
    if (s[i]=="@" and t[i] in l) or (t[i]=="@" and s[i] in l):
      pass
    else:
      ans = "You will lose"
print(ans)