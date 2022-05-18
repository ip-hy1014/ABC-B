n,a,b = map(int,input().split())
s,d = [],[]
for _ in range(n):
  x,y = input().split()
  s.append(x)
  d.append(int(y))
ans = 0
for i in range(n):
  if s[i]=="East":
    if d[i]<a:
      ans += a
    if a<=d[i]<=b:
      ans += d[i]
    if d[i]>b:
      ans += b
  if s[i]=="West":
    if d[i]<a:
      ans -= a
    if a<=d[i]<=b:
      ans -= d[i]
    if d[i]>b:
      ans -= b
if ans==0:
  print(0)
elif ans>0:
  print("East",ans)
else:
  print("West",abs(ans))