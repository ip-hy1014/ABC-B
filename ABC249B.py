s = input()
if not s.isupper() and not s.islower() and len(s) == len(set(s)):
  print("Yes")
else:
  print("No")