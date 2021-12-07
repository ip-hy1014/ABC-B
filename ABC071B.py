s = input()
l = "abcdefghijklmnopqrstuvwxyz"
for i in l:
  if i not in s:
    print(i)
    exit()
print("None")