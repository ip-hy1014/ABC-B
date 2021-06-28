n,m = map(int ,input().split())
ka = set(map(int, input().split()[1:]))
for _ in range(n-1):
  ka = ka & set(map(int, input().split()[1:]))
print(len(ka))