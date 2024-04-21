n = int(input())
t, i = 0, 1
res = 0
while t <= n:
    if n - t == i:
        break
    if n - t < i:
        i = 1
        if n - t == i:
            break
    t += i
    i += 1
    res += 1
print(res+1)