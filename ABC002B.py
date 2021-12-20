w = input()
print(w.replace('a','').replace('i','').replace('u','').replace('e','').replace('o',''))

#別解
w = input()
l = 'aiueo'
for i in w:
  if i not in l:
    print(i,end='')
print()
