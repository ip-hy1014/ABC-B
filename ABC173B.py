from collections import Counter

n = int(input())
s = [input() for _ in range(n)]
counter = Counter(s)
output = ['AC', 'WA', 'TLE', 'RE']

for key in output:
  print(f"{key} x {counter[key]}")

#別解
n = int(input())
s = [input() for _ in range(n)]
print("AC x " + str(s.count("AC")))
print("WA x " + str(s.count("WA")))
print("TLE x " + str(s.count("TLE")))
print("RE x " + str(s.count("RE")))