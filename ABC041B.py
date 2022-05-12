a,b,c = map(int,input().split())
mod = 10**9+7
print(a*b*c%mod)

#golf
print(eval(input().replace(' ','*'))%(10**9+7))

print(eval(input().replace(*' *'))%(10**9+7))