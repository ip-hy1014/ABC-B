"""
問題文
AtCoder国には N 個の山があり、i 個目の山の名前は Si, 高さは Ti です。
2 番目に高い山の名前を答えてください。
N 個の山の名前、高さはそれぞれ相異なることが保証されます。
"""

n = int(input())
data = []
for i in range(n):
  s,t = map(str, input().split())
  t = int(t)
  data.append([t,s])
data.sort(reverse=True)
print(data[1][1])