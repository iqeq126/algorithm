import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = set(input().rstrip() for _ in range(N))
res = list()
for i in range(M):
    sub_string = input().rstrip()
    if sub_string in S:
        res.append(sub_string)
print(len(res))