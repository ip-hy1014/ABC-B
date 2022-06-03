n,x = map(int,input().split())
a = list(map(int,input().split()))
b = str(bin(x))[2:]
ans = 0
for i in range(1,len(b)+1):
  if b[-i]=="1":
    ans += a[i-1]
print(ans)