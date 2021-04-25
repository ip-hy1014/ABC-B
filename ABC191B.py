"""
問題文
長さ N の整数列 A と整数 X が与えられます。
A から X と等しい要素を全て取り除き、残った要素をそのままの順序で並べた数列 A′ を出力してください。
"""

n, x = map(int, input().split())
a = list(map(int, input().split()))
print(" ".join([str(i) for i in a if i != x]))

