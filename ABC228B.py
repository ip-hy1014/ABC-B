n,x = map(int,input().split())
a = list(map(int,input().split()))
b = [False]*(n)
while not b[x-1]:
  b[x-1] = True
  x = a[x-1]
print(b.count(True))