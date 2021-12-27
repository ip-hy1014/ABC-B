a,b,k = map(int,input().split())
if b-a+1>2*k:
  for i in range(a,a+k):
    print(i)
  for i in range(b-k+1,b+1):
    print(i)
else:
    for i in range(a,b+1):
      print(i)

#別解
a,b,k = map(int,input().split())
ans = set()
for i in range(a,a+k):
  if a<=i<=b:
    ans.add(i)
for i in range(b,b-k,-1)[::-1]:
  if a<=i<=b:
    ans.add(i)
ans = sorted(list(ans))
for i in ans:
  print(i)
