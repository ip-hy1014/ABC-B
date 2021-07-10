n,x = map(int, input().split())
a = list(map(int, input().split()))
a_o = sum(a[::2])
a_e = a[1::2]
a_e_s = sum(a_e) - len(a_e)*1
if a_o + a_e_s <= x:
  print("Yes")
else:
  print("No")

#別解
N, X = map(int, input().split())
A = list(map(int, input().split()))
if sum(A) - N//2 <= X :
    print("Yes")
else:
    print("No")