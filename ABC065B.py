n = int(input())
a = [int(input()) for _ in range(n)]
c = 1
for i in range(n+1):
  c = a[c-1]
  if c==2:
    print(i+1)
    exit()
print(-1)