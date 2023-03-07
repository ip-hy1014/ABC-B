n,k = map(int,input().split())
s = input()
ans =""
for i in s:
  if i=="o" and ans.count("o")<k:
    ans+="o"
  else:
    ans+="x"
print(ans)