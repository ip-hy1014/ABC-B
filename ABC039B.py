import math
n = int(input())
ans = math.sqrt(math.sqrt(n))
print(int(ans))

#別解
n = int(input())
ans = (n**0.5)**0.5
print(ans)