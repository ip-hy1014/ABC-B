l = sorted(list(map(int,input().split())))
k = int(input())
ans = l[-1]*2**k
print(sum(l[:2])+ans)