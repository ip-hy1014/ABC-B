n = int(input())
s = input()
f = s.find("1")
if f%2==0:
    print("Takahashi")
else:
    print("Aoki")

#別解
n = int(input())
s = input()
for i in range(n):
  if s[i] == "1":
    if i%2==0:
      print("Takahashi")
    else:
      print("Aoki")
    break