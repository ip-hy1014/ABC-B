n,k,q = map(int,input().split())
a = list(map(int,input().split()))
l = list(map(int,input().split()))
for i in range(q):
  if a[l[i]-1]==n:
    continue
  elif l[i]==k:
    a[l[i]-1]+=1
  elif a[l[i]-1]+1 < a[l[i]]:
    a[l[i]-1]+=1
print(*a)

#別解
n,k,q = map(int,input().split())
a = list(map(int,input().split()))
l = list(map(int,input().split()))
for i in l:
  if a[i-1]<n and a[i-1]+1 not in a: #コマがマスの一番右にない かつ コマを一つ右に動かした状態と同じ状態のコマがaにないなら右に1つ動かす
    a[i-1]+=1
print(*a)