s = input()
for i in range(1,len(s)):
  t = s[:-i]
  if t[:len(t)//2] == t[len(t)//2:]:
    print(len(t))
    exit()