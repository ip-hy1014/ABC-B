s = input()
ans = 0
n = len(s)
for i in range(n):
  if s[i] != s[n-1-i]: #最初の文字と最後の文字を比較,2文字目と最後から2文字目を比較...
    ans += 1
print(ans//2)