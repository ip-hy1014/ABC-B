a,b,c = map(int,input().split())
d = a+b
e = a-b
if c == d and c != e:
  print("+")
elif c == e and c != d:
  print("-")
elif c == d and c == e:
  print("?")
else:
  print("!")