print(-1 if input()=="a" else "a")

#別解
s = input()
def alpha2num(alpha):
    num=0
    for index, item in enumerate(list(alpha)):
        num += pow(26,len(alpha)-index-1)*(ord(item)-ord('A')+1)
    return num
n = alpha2num(s)-1
def a(n):
  if n<=26:
    return chr(64+n)
  elif n%26==0:
    return a(n//26-1)+chr(90)
  else:
    return a(n//26)+chr(64+n%26)
if s=="a":
  print(-1)
else:
  print(a(n).lower()[0])
