N,T = map(int, input().split())
l = []
for i in range(N):
  n,t = map(int, input().split())
  l.append([n,t])
l.sort(reverse=False) #コスト昇順に並び替え
for i in range(N):
  if l[i][1] <= T:
    print(l[i][0])
    exit()
print("TLE")

#別解
n,t = map(int,input().split())
c = []
for i in range(n):
    c1,t1 = map(int,input().split())
    if t1 <= t: #最初からt以下のコストのみでリスト作成
      c.append(c1)
print("TLE" if len(c)==0 else min(c)) #リストが空ならTLE