import sys
input = sys.stdin.readline
n, m = map(int, input().split())
res = [0] * m
big = 0
for i in range(n):
    num = input().rstrip('\n')
    res[i] = num
    big = max(big, int(num))
for i in range(m-n):
    res[n+i] = str(big)
print(*sorted(res, key = lambda x: x*10, reverse=True), sep="")