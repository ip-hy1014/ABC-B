g = 100
ans = 0
x = int(input())
while True:
   if g>=x:
       print(ans)
       break
   g += g//100
   ans += 1