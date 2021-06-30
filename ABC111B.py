import math
n = int(input())
a = math.ceil(n/111)
print(a*111)

#別解
n = int(input())
print(n if n%111==0 else (n//111+1)*111)