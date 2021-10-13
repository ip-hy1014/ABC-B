n = int(input())
m = str(n)
l = sum(list(map(int,m)))
print("Yes" if n%l==0 else "No")