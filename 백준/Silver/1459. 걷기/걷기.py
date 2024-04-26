lst = list(map(int, input().split()))
x, y = lst[0], lst[1]
if lst[2] > lst[3]:
    if (y-x) % 2 == 0:
        print(max(x, y) * lst[3])
    else:
        print((max(x, y)-1) * lst[3] + lst[2])
elif 2*lst[2] <= lst[3]:
    print(lst[2] * (x + y))
else:
    print(min(x, y) * lst[3] + abs(x- y) * lst[2])