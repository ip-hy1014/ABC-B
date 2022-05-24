a = list(input())
b = list(input())
c = list(input())
p = a.pop(0)
while True:
  if p=="a":
    if len(a)==0:
      print("A")
      break
    else:
      p = a.pop(0)
  elif p=="b":
    if len(b)==0:
      print("B")
      break
    else:
      p = b.pop(0)
  else:
    if len(c)==0:
      print("C")
      break
    else:
      p = c.pop(0)