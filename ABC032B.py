s = input()
k = int(input())
se = set()
for i in range(len(s)-k+1):
  se.add(s[i:i+k])
print(len(se))