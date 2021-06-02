#TLE
n,a,b = map(int, input().split())
B = "b"*a
R = "r"*b
for _ in range(10**100):
  c = B + R
ans = c[:n]
print(ans.count("b"))

#正答
n,a,b = map(int, input().split())
ans = n//(a+b)*a
r = n%(a+b)
ans += min(r,a)
print(ans)