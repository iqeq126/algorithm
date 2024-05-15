import sys
input = lambda : sys.stdin.readline()
n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]
res = 0
for i in range(n):
    tar = belt[:k]
    l = len(set(tar))
    if c not in tar:
        l += 1
    if l > res:
        res = l
    belt = belt[-1:] + belt[:-1]
print(res)