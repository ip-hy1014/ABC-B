w,h,n = map(int,input().split())
x,y = 0,0
for _ in range(n):
  a,b,c = map(int,input().split())
  if c==1:
    x = max(x,a)
  elif c==2:
    w = min(w,a)
  elif c==3:
    y = max(y,b)
  else:
    h = min(h,b)
print(max(w-x,0)*max(h-y,0))