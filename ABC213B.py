n = int(input())
a = list(map(int,input().split()))
b = sorted(a)
c = b[-2]
print(a.index(c)+1)