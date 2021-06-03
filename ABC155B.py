n = int(input())
a = list(map(int, input().split()))

c1=0
c2=0

for i in range(n):
  if a[i] % 2 == 0:
    c1 += 1
    if a[i] % 3 == 0 or a[i] % 5 == 0:
      c2 += 1

if c1==c2:
  print("APPROVED")
else:
  print("DENIED")

#all 全ての要素がTrueならTrueを返す
n = int(input())
a = list(map(int, input().split()))
if all(i % 3 == 0 or i % 5 == 0 for i in a if i % 2 == 0):
  print("APPROVED")
else:
  print("DENIED")

#偶数かつ3でも5でも割り切れないものがあったらDENIED
n = int(input())
a = list(map(int, input().split()))
ans = "APPROVED"
for i in range(n):
  if a[i] % 2 == 0 and a[i] % 3 != 0 and a[i] % 5 != 0:
    ans = "DENIED"
print(ans)