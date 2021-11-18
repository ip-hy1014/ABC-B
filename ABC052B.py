n = int(input())
s = input()
c = 0
ans = 0
for i in s:
  if i=="I":
    c += 1
  else:
    c -= 1
  ans = max(ans,c)
print(ans)

#別解
n = int(input())
s = input()
x = 0
l = [0]
for i in s:
  if i=="I":
    x+=1
    l.append(x)
  else:
    x-=1
    l.append(x)
print(max(l))