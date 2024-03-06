import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
lst = sorted(list(map(int, input().split())))
s, e = 0, N-1
res = 0
while s < e:
    lst_sum = lst[s] + lst[e]
    s += 1; e -= 1
    if lst_sum == M: res += 1
    if lst_sum < M: e += 1
    if lst_sum > M: s -= 1
print(res)