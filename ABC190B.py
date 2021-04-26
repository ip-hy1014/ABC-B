"""
問題文
魔法使いの高橋君は魔物と戦っています。
高橋君は N 種類の呪文を使うことができます。
i 番目の呪文は詠唱に Xi 秒かかり、威力は Yi です。
ただし、この魔物は強いので、詠唱に S 秒以上かかる呪文や、威力が D 以下の呪文ではダメージを与えられません。 また、呪文以外の方法でダメージを与えることもできません。
高橋君は魔物にダメージを与えられるでしょうか？

出力
魔物にダメージを与えられるならば Yes を、与えられないならば No を出力せよ。
"""


def ans():
  for _ in range(n):
    x, y = map(int, input().split())
    if x < s and y > d:
      return True
  return False
n, s, d = map(int, input().split())
print("Yes" if ans() else "No")

#公式解答
N, S, D = map(int, input().split())
def check():
    X, Y = map(int, input().split())
    return X < S and Y > D

if any(check() for i in range(N)):
    print("Yes")
else:
    print("No")
