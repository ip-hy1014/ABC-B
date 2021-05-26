n = int(input())
print("Yes" if n % 9 == 0 else "No")

#別解
n = input()
tmp = 0
for i in n:
  tmp += int(i)
print("Yes" if tmp%9==0 else "No")