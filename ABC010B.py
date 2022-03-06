n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in a:
  if i==1:
    pass
  elif i==2:
    ans += 1
  elif i==3:
    pass
  elif i==4:
    ans += 1
  elif i==5:
    ans += 2
  elif i==6:
    ans += 3
  elif i==7:
    pass
  elif i==8:
    ans += 1
  else:
    pass
print(ans)

n = int(input())
a = list(map(int,input().split()))
ans = 0
for i in a:
  while i % 2 == 0 or (i-2) % 3 == 0:
    ans += 1
    i -= 1
print(ans)