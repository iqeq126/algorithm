import sys
input = sys.stdin.readline
n = int(input())
weights = sorted(list(map(int, input().split())))
res = 1
for weight in weights:
    if res < weight:
        break
    res += weight
print(res)