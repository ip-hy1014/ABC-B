n,X,Y,Z = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
me = []
for i,(m,e) in enumerate(zip(a,b)):
  me.append((i+1,m,e,m+e)) #受験生番号、数学の点数、英語の点数、合計点数をappend
ans = []
me.sort(key=lambda x:(x[1],-x[0])) #数学の点数でソート、点数が同じ場合は受験生番号が小さい方をappendするために-x[0]を指定
for _ in range(X):
  ans.append(me.pop()[0]) #インデックスで0を指定することで受験生番号のみをpopし、それをappendする
me.sort(key=lambda x:(x[2],-x[0])) #英語の点数でソート
for _ in range(Y):
  ans.append(me.pop()[0])
me.sort(key=lambda x:(x[3],-x[0])) #合計点数でソート
for _ in range(Z):
  ans.append(me.pop()[0])
ans.sort()
print(*ans)