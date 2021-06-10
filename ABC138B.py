n = int(input())
a = list(map(int, input().split()))
print('{:.16g}'.format(1 / sum(1 / i for i in a)))