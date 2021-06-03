#必要な点数は n*m
#N科目目を残して目標点数未満の場合は，n*m - sum(a)
#N科目目以前に目標点数に到達している場合は，0
#k < n*m - sum(a) の場合は,-1

n,k,m = map(int, input().split())
a = list(map(int, input().split()))
if n*m - sum(a) <= k:
  print(max(0,n*m-sum(a)))
else:
  print(-1)