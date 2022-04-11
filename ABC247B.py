n = int(input())
S = []
T = []
for _ in range(n):
  s,t = input().split()
  S.append(s)
  T.append(t)
for i in range(n):
  ok = False
  for x in [S[i],T[i]]:
    ok2 = True
    for j in range(n):
      if i!=j:
        if x==S[j] or x==T[j]:
          ok2 = False
    if ok2 == True:
      ok = True
  if ok == False:
    print("No")
    exit()
print("Yes")