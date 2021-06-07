#sのi文字目,i+1文字目,i+2文字目を取り出して最も753に近いものを採用する．
s = input()
print(min(abs(int(s[i:i+3]) - 753) for i in range(len(s) - 2)))