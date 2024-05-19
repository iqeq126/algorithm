from itertools import permutations
import sys
print = sys.stdout.write
n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
comb = permutations(lst, m)
s=set()
for c in comb:
    if c not in s:
        for j in range(m):
            print(f"{c[j]} ")
        print("\n")
    s.add(c)