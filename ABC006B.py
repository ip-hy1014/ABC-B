n = int(input())
mod = 10007
l = [0,0,1]
for i in range(3,n):
  l.append((l[i-1]+l[i-2]+l[i-3])%mod)
print(l[n-1])