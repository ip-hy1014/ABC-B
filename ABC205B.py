n = int(input())
a = list(map(int, input().split()))
b = set(a)
print("Yes" if n == len(b) else "No")