import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
res, sum_lst = 0, sum(lst)
for i in range(n-1):
    sum_lst -= lst[i]
    res += lst[i] * sum_lst
print(res)