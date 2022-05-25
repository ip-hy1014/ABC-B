n,l = map(int,input().split())
s = [input() for _ in range(n)]
s.sort()
print("".join(s))

#golf
n = (sorted((open(0).read().split()[2:])));print(*n,sep="")