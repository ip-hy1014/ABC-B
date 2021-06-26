a,b,c,d = map(int, input().split())
e = 0
for i in range(10**6):
  if a <= e*d:
    print(i)
    break
  a += b
  e += c
else:
  print(-1)

#別解
a,b,c,d = map(int, input().split())
ans = -1
e = c*d-b
if 0 < e:
  ans = (a+e-1)//e
print(ans)
