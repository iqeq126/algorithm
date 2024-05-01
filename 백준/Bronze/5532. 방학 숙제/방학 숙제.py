import math
lst = [0] * 5
for _ in range(5):
    lst[_] = int(input())

res1, res2 = math.ceil(lst[1] / lst[3]), math.ceil(lst[2] / lst[4])
print(lst[0] - max(res1, res2))