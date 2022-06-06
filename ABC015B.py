import math
n = int(input())
a = list(map(int,input().split()))
s = 0
c = 0
for i in a:
  if i==0:
    continue
  else:
    s += i
    c += 1
print(math.ceil(s/c))

#別解
n = int(input())
a = list(map(int,input().split()))
c = a.count(0)
s = 0--sum(a)//(n-c) #切り上げ
print(s)
