from itertools import combinations
while True:
    lst = list(map(int, input().split()))
    if lst[0] == 0: 
        break
    lst = lst[1:]
    comb = combinations(lst, 6)
    s=set()
    for c in comb:
        print(*c)
    print()