a = list(map(int,input().split()))
b = list(map(int,input().split()))
l = len(set(a)&set(b))
print("YES" if l>0 else "NO")