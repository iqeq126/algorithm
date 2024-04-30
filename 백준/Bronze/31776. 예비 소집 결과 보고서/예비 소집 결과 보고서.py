import sys
input = sys.stdin.readline
n = int(input())
res = 0
for i in range(n):
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        continue
    if 0 <= a <= b <= c or (0 <= a <= b and c == -1) or (a >= 0 and b == c == -1):
        res += 1
print(res)