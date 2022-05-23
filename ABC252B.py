n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = [i for i,j in enumerate(a) if j == max(a)]
ans = "No"
for i in c:
  if i+1 in b:
    ans = "Yes"
print(ans)