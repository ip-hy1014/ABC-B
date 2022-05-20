n = int(input())
ab = list(map(int,input().split()))
k = int(input())
p = list(map(int,input().split()))
l = ab+p
s = set(l)
print("YES" if len(l)==len(s) else "NO")