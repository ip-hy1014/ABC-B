from itertools import combinations
n,w = map(int,input().split())
a = list(map(int,input().split())) + [0,0] #3個以下を選ぶ際、1個・2個の場合で分けるのは面倒であるから重さが0のおもりが2つあることにする。
ok = [False]*(w+1) #良い整数かを管理するための配列を用意、Falseで初期化
for x,y,z in combinations(a,3): #全探索する
  ans = x+y+z
  if ans<=w:
    ok[ans] = True #おもりの重量合計がw以下だったらTrueにする
print(ok.count(True))