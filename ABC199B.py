"""
問題文
長さ N の数列 A=(A1,A2,A3,…,AN),B=(B1,B2,B3,…,BN) が与えられます。
以下の条件を満たす整数 x の個数を求めてください。
1≤i≤N を満たす全ての整数 i について Ai≤x≤Bi
"""

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = 0
for i in range(1, 1001) :
	ok = True
	for j in range(n) :
		if i < a[j] or i > b[j] : ok = False
	if ok : res += 1

print(res)


