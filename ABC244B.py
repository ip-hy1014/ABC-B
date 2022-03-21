n = int(input())
t = input()
x = 0
y = 0
c = 0
for i in t:
  if i=="S":
    if c==0:
      x+=1
    if c==1:
      y-=1
    if c==2:
      x-=1
    if c==3:
      y+=1
  if i=="R":
    c = (c+1)%4
print(x,y)