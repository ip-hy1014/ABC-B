n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
print(b[-1]-b[0])

#別解
n = int(input())
a = list(map(int, input().split()))
print(max(a)-min(a))