#倒れてたら○、倒れてなかったら×
s = "0"+input()
if s[1]=="1":
  print("No")
  exit()
c = "" #列の管理
if s[7]=="1":
  c+="×"
else:
  c+="○"
if s[4]=="1":
  c+="×"
else:
  c+="○"
if s[2]=="1" or s[8]=="1":
  c+="×"
else:
  c+="○"
if s[5]=="1":
  c+="×"
else:
  c+="○"
if s[3]=="1" or s[9]=="1":
  c+="×"
else:
  c+="○"
if s[6]=="1":
  c+="×"
else:
  c+="○"
if s[10]=="1":
  c+="×"
else:
  c+="○"
if "×○×" in c:
  print("Yes")
elif "×○○×" in c:
  print("Yes")
elif "×○○○×" in c:
  print("Yes")
elif "×○○○○×" in c:
  print("Yes")
elif "×○○○○○×" in c:
  print("Yes")
else:
  print("No")