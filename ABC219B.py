s1 = input()
s2 = input()
s3 = input()
l = []
l2 = []
l.append(s1)
l.append(s2)
l.append(s3)
t = input()
for i in range(len(t)):
  l2.append((l[int(t[i])-1]))
print(*l2,sep="")

#別解
s = [input() for _ in range(3)]
t = input()
ans = ""
for i in range(len(t)):
    ans += s[int(t[i])-1]
print(ans)