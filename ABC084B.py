n,m = map(int,input().split())
s = input()
a = s[n]
b = s[:n]
c = s[n+1:]
if a=="-" and b.isdigit() and c.isdigit():
  print("Yes")
else:
  print("No")