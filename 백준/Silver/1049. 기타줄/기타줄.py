n, m = map(int, input().split())
lst = []
for _ in range(m):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: x[0])
res = ( n // 6 ) * lst[0][0]
buf = lst[0][0]
lst.sort(key=lambda x: x[1])
res += min( buf, ( n % 6) * lst[0][1])
print(min(res, n * lst[0][1]))