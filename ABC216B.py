n = int(input())
l = []
for _ in range(n):
	l.append(input().split())
a = list(map(list,set(map(tuple,l))))
if n == len(a):
	print("No")
else:
	print("Yes")