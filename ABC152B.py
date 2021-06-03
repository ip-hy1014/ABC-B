a,b = input().split()
a_l = a*int(b)
b_l = b*int(a)

if int(a_l[:1]) <= int(b_l[:1]):
  print(a_l)
else:
  print(b_l)

#別解
a,b = map(int, input().split())
print(str(min(a,b))*max(a,b))

#別解
a,b = sorted(input().split())
print(a*int(b))