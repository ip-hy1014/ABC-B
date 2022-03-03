n = int(input())
a = [int(input()) for _ in range(n)]
s = list(set(a))
s.sort()
print(s[-2])