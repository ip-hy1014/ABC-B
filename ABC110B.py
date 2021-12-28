n,m,X,Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
for i in range(-100, 101):
  if X < i <= Y and max(x) < i <= min(y):
    print("No War")
    exit()
print("War")

#別解
n,m,x,y = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
mx = max(a)
mn = min(b)
ans = "War"
for i in range(x,y+1):
  if mx<i<=mn and x<i<=y:
    ans = "No War"
    break
print(ans)
