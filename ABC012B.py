n = int(input())
h = n//3600
m = n//60%60
s = n%60
print(str(h).zfill(2), str(m).zfill(2), str(s).zfill(2), sep=":")