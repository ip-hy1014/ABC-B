n = int(input())
s = set(list(map(str,input().split())))
print("Four" if len(s)==4 else "Three")