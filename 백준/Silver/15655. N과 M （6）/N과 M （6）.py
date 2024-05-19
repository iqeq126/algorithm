from itertools import combinations
n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
comb = combinations(lst, m)
for c in comb:
    print(*c)