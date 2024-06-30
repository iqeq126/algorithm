import copy
import sys
input = sys.stdin.readline
n = int(input())
max_lst = list(map(int, input().split()))
min_lst = copy.deepcopy(max_lst)

for i in range(n-1):
    a, b, c = map(int, input().split())
    M0, M1, M2 = max_lst[0], max_lst[1], max_lst[2]
    m0, m1, m2 = min_lst[0], min_lst[1], min_lst[2]

    max_lst[0], max_lst[1], max_lst[2] \
        = max(M0, M1) +a, max(M0, M1, M2) + b, max(M1, M2) + c

    min_lst[0], min_lst[1], min_lst[2] \
        = min(m0, m1) +a, min(m0, m1, m2) + b, min(m1, m2) + c

print(max(max_lst), min(min_lst))