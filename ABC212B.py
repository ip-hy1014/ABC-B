l = input()
a = int(l[0])
b = int(l[1])
c = int(l[2])
d = int(l[3])
if len(set(l)) == 1:
  print("Weak")
  exit()
if (a+1)%10 == b and (b+1)%10 == c and (c+1)%10 == d:
  print("Weak")
else:
  print("Strong")

#別解
X = input()
weak = ['0123','1234','2345','3456','4567','5678','6789','7890','8901','9012']
if X[0] == X[1] and X[1] == X[2] and X[2] == X[3]:
    print('Weak')
elif X in weak:
    print('Weak')
else:
    print('Strong')