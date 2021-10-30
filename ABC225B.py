n = int(input())
c = [0]*n
for _ in range(n-1):
  a,b = map(int,input().split())
  c[a-1]+=1
  c[b-1]+=1
print("Yes" if max(c)==n-1 else "No")