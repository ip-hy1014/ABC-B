n,m = map(int,input().split())
a = 30*(n%12)+(0.5*m)
b = 6*m
print(min(abs(a-b),360-abs(a-b)))