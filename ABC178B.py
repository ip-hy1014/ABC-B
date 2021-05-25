"""
問題文
整数 a,b,c,d が与えられます。
a≤x≤b,c≤y≤d を満たす整数 x,y について、x×y の最大値はいくつですか。
"""

a,b,c,d = map(int, input().split())
print(max(a*c,a*d,b*c,b*d))