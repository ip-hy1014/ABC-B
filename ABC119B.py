n = int(input())
ans = 0
for i in range(n):
  x,u = input().split()
  x = float(x)
  if u == "BTC":
    ans += x*380000
  else:
    ans += x
print(ans)
