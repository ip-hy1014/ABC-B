"""
問題文
整数または小数 X が与えられるので、小数点以下を切り捨てて整数で出力してください。
"""

from decimal import *
X = Decimal(input())
print(int(X))

#別解
X = input()
a = X.split('.')[0]
print(a)

"""
文字列として受け取って . 小数点部分で分割し，左側だけ出力する
"""