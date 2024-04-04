n, l = map(int, input().split())
lst = sorted(list(map(int, input().split())))
res, now = 1, lst[0]
for i in range(1, n):
    if l <= lst[i] - now:
        res += 1
        now = lst[i]
print(res)