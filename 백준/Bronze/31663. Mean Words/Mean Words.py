n = int(input())
lst = []
res = [0] * 45
times = [0] * 45
for i in range(n):
    lst.append(input().rstrip('\n'))
i = 0
for s in lst:
    for j in range(len(s)):
        res[j] += ord(lst[i][j])
        times[j] += 1
    i += 1
for i in range(45):
    if res[i] > 0 and times[i] > 0:
        c = res[i] // times[i]
        if ord('a') <= c <= ord('z'):
            print(chr(c), end="")