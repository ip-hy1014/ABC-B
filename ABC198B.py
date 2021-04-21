"""
問題文
整数 N が与えられます。
N を十進法で表した文字列の先頭に 0 個以上の 0 をつけることで、回文にすることはできますか？

出力
回文にできるなら Yes、できないなら No を出力せよ。
"""

n = input()
def judge():
  for i in range(10):
    z = "0" * i
    t = z + n
    if t == t[::-1]:
      return True
  return False
if judge():
    print("Yes")
else:
    print("No")

"""
文字列の逆順は 文字列[::-1]となる。
"""