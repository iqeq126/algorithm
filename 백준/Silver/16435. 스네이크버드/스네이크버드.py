n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
res = m
for i in range(n):
    if res >= lst[i]:
        res += 1
print(res)