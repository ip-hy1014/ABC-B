p = list(map(int,input().split()))
p_ = []
for i in p:
  p_.append(chr(i+64)) #大文字
l = []
for i in range(len(p)):
  l.append(p_(i))
  l = list(map(str.lower,l))

#別解
plst = list(map(int, input().split()))
for p in plst:
    print(end = chr(96 + p)) #小文字