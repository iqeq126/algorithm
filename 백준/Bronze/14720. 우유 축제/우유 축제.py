n = int(input())
lst = list(map(int, input().split()))
tag, res = -1, 0
for i in range(n):
    if lst[i] == 0 and tag == -1:
        tag = 0
        res += 1
        continue
    elif lst[i] == 1 and tag == 0:
        tag = 1
        res += 1
        continue
    elif lst[i] == 2 and tag == 1:
        tag = 2
        res += 1
        continue
    elif lst[i] == 0 and tag == 2:
        tag = 0
        res += 1
        continue
print(res)