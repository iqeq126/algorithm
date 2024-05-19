from itertools import combinations
n, m = map(int, input().split())
lst = sorted(list(input().strip('\n').split()))
comb = combinations(lst, n)
s=set()
for c in comb:
    l = len(set('aeiou').intersection(c))
    if l > 0 and len(c) - l >= 2:
        print(*c, sep="")