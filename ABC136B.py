#桁数を文字列に変換してその長さを2で割った時の余りで判定
n = int(input())
ans = 0
for i in range(1, n+1):
  if len(str(i)) % 2 == 1:
    ans += 1
print(ans)