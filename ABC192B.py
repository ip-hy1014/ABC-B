"""
問題文
先頭から奇数番目の文字が全て英小文字であり、かつ、先頭から偶数番目の文字が全て英大文字であるような文字列を 読みにくい文字列 と呼びます。
文字列 S が読みにくい文字列かどうか判定してください。

出力
S が読みにくい文字列なら Yes、読みにくい文字列でないなら No を出力せよ。
"""

s = input()
if len(s) == 1:
  print("Yes" if s.islower() else "No")
else:
    A = s[::2]
    B = s[1::2]
    print("Yes" if A.islower() and B.isupper() else "No")