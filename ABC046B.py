n,k = map(int,input().split())
ans = k
for _ in range(n-1):
  ans *= k-1
print(ans)

#golf
n,k = map(int,input().split());print(k*(k-1)**~-n)