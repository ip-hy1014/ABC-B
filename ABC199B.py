"""
問題文
長さ N の数列 A=(A1,A2,A3,…,AN),B=(B1,B2,B3,…,BN) が与えられます。
以下の条件を満たす整数 x の個数を求めてください。
1≤i≤N を満たす全ての整数 i について Ai≤x≤Bi
"""

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

max_a = max(a)
min_b = min(b)

if max_a <= min_b:
    print(min_b - max_a + 1)
else:
    print(0)

"""
xの個数は数列Bの最小値から数列Aの最大値を引いた値 + 1．
それ以外のときは0を出力する．
"""
