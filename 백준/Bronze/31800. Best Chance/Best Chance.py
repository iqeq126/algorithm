import sys
input = sys.stdin.readline
n = int(input())
benefit = list(map(int, input().split()))
price = list(map(int, input().split()))
buf = sorted(benefit, reverse=True)
res = [0] * n
for i in range(n):
    if benefit[i] != buf[0]:
        chance = buf[0] - price[i]
    else:
        chance = buf[1] - price[i]
    res[i] = benefit[i] - chance - price[i]
print(*res)