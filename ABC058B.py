o = input()
e = input()
ans = ""
a = 0
b = 0
for i in range(len(o)+len(e)):
  if i%2==0:
    ans += o[a]
    a+=1
  else:
    ans += e[b]
    b+=1
print(ans)