s = input()
ans = ""
for i in s:
  if i=="0" or i=="1":
    ans += i
  else:
    ans = ans[:-1]
print(ans)