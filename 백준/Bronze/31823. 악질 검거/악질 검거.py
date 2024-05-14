import sys
input = lambda : sys.stdin.readline()
n,m = map(int, input().split())
result = []
s = set()
for i in range(n):
    lst = list(input().split())
    res, local_res = 0, 0
    for j in range(m):
        if lst[j] == '.':
            local_res += 1
        else:
            res = max(res, local_res)
            local_res = 0
    s.add(max(res, local_res))
    result.append([ max(res, local_res), lst[-1] ])
print(len(s))
for i in range(n):
    print(*result[i])