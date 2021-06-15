n,l = map(int,input().split())
L = l
R = n+l-1
a = 0
if R <= 0:
  a = R
elif L >= 0:
  a = L
else:
  a = 0
ans = int((R+L)*(R-L+1)/2 - a)
print(ans)