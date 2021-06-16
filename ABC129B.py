n = int(input())
w = list(map(int, input().split()))
s = sum(w)
for i in range(n):
  s = min(s, abs(sum(w[i+1:]) - sum(w[:i+1])))
print(s)