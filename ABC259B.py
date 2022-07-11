import math
a,b,d = map(int,input().split())
r = math.radians(d)
ansx = a*math.cos(r)-b*math.sin(r)
ansy = a*math.sin(r)+b*math.cos(r)
print(ansx,ansy)