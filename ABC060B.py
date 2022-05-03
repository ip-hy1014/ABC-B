a,b,c = map(int,input().split())
ans = "NO"
for i in range(a,b*a+1):
  if i*a%b==c:
    ans = "YES"
print(ans)