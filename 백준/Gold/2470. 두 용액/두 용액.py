import sys
sys.setrecursionlimit(10 ** 8)
INF = sys.maxsize
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
lst.sort()
global L, R, res
L, R = -INF, INF
res = INF
def binary_search(l, r):
    global L, R, res
    mid = lst[l] + lst[r]
    if l < r:
        if res > abs(mid):
            L, R = lst[l], lst[r]
            res = abs(mid)
            if mid == 0:
                print(*sorted([L, R]))
                return
        if mid < 0:
            binary_search(l+1, r)
        else:
            binary_search(l, r-1)
    else:
        print(*sorted([L, R]))
        return
binary_search(0, N-1)