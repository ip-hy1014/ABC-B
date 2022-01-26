n = int(input())
s = input()
mx = 0
for i in range(1,n):
  c = set(s[:i]) & set(s[i:])
  mx = max(mx,len(c))
print(mx)