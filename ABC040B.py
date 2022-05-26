n = int(input())
mn = 10**18
for i in range(1,n+1):
  j = n//i
  for k in range(1,j+1):
    mn = min(mn,abs(i-j)+(n-i*j))
print(mn)