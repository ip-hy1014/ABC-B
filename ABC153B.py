h,n = map(int, input().split())
a = list(map(int, input().split()))
print("Yes" if sum(a)>=h else "No")

#別解
h,n = map(int, input().split())
a = sum(map(int, input().split()))
print("Yes" if a>=h else "No")