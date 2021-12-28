s = input()
a = [0]*6
for i in s:
  if i=="A":
    a[0]+=1
  elif i=="B":
    a[1]+=1
  elif i=="C":
    a[2]+=1
  elif i=="D":
    a[3]+=1
  elif i=="E":
    a[4]+=1
  else:
    a[5]+=1
print(a)

#別解
s = input()
l = "ABCDEF"
ans = []
for i in l:
  ans.append(s.count(i))
print(*ans)