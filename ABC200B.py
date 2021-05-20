"""
問題文
整数 N が与えられます。
以下の操作を K 回行った後の整数 N を出力してください。
整数 N が 200 の倍数であれば、N を 200 で割る。
そうでなければ、整数 N を、N の後ろに文字列として 200 を付け加えた整数に置き換える。
例えば、7 を置き換えると 7200 に、1234 を置き換えると 1234200 になります。
"""

n,k = map(int, input().split())
for i in range(k):
    if n % 200 == 0:
      n = n//200
    else:
      n = n*1000+200
print(n)

#別解
n,k=map(int,input().split())
for i in range(k):
    if(n%200==0):
        n//=200
    else:
        s=str(n)
        s+="200"
        n=int(s)
print(n)