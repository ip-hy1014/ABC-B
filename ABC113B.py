n = int(input())
t,a = map(int, input().split())
h = list(map(int, input().split()))
b = []
for i in range(n):
  b.append(abs(a-(t-h[i]*0.006)))
print(b.index(min(b))+1)