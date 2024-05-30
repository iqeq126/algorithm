import sys
input = sys.stdin.readline
n = int(input())
lst = sorted(list(map(int, input().split())))
res = sys.maxsize
for i in range(n-3):
    for j in range(i+3, n):
        l, r = i+1, j-1
        while l < r:
            s1, s2 = lst[i]+lst[j], lst[l] + lst[r]
            loc = s2 - s1
            res = min(res, abs(loc))
            if loc > 0:
                r -= 1
            else:
                l += 1
print(res)