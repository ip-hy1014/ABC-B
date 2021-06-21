s = input()
l = int(s[:2])
r = int(s[2:])
if 0<l<13 and 0<r<13:
  print("AMBIGUOUS")
elif 0<=l and 0<r<13:
  print("YYMM")
elif 0<l<13 and 0<=r:
  print("MMYY")
else:
  print("NA")