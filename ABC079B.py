import functools
@functools.lru_cache()
def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)
print(lucas(int(input())))

#別解
n = int(input())
l = [2,1] #初項と次項を持っておく
for i in range(2,n+1):
  l.append(l[i-1] + l[i-2])
print(l[n])