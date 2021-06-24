a,b,k = map(int, input().split())
l=[]
for i in range(1,101):
  if a % i == 0 and b % i == 0:
    l.append(i)
print(l[-k])

#別解
a,b,k = map(int, input().split())
l = [i for i in range(1,101) if a%i==0 and b%i==0]
print(l[-k])