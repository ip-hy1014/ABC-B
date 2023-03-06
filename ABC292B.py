n,q = map(int,input().split())
l = [0]*n
for i in range(q):
  a,b = map(int,input().split())
  if a == 3:
    if l[b-1]>=2:
      print("Yes")
    else:
      print("No")
  elif a == 1:
    l[b-1]+=1
  elif a == 2:
    l[b-1]+=2