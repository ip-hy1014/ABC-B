n,m = map(int, input().split())
A = list(map(int, input().split()))
c = 0
for a in A:
  if a >= sum(A)/(4*m):
    c += 1
print("Yes" if c>=m else "No")