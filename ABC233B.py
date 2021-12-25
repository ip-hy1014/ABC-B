l,r = map(int,input().split())
s = input()
a = s[:l-1]
b = s[r:]
c = s[l-1:r][::-1]
print(a+c+b)