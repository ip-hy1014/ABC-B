from collections import Counter
w = input()
c = Counter(w)
ans = True
for i in c.values():
  if i%2!=0:
    ans = False
if ans:
  print("Yes")
else:
  print("No")