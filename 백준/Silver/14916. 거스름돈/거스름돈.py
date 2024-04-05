n = int(input())
lst = [-1] * 100001
lst[2], lst[5] = 1, 1
for i in range(3, n+1):
    if lst[i-2] >= 0:
        lst[i] = lst[i-2] + 1
    if lst[i - 5] >= 0:
        lst[i] = min(lst[i], lst[i-5] + 1)
print(lst[n])