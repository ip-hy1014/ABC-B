n = int(input())
p = [int(input()) for i in range(n)]
a = sorted(p)
print(int((sum(p)-a[-1]+(a[-1]/2))))

#別解
n = int(input())
p = [int(input()) for i in range(n)]
print(sum(p)-max(p)//2)