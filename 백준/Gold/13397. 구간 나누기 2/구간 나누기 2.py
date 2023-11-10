import sys
sys.setrecursionlimit(10 ** 8)
INF = sys.maxsize
input = sys.stdin.readline
N, M  = map(int, input().split())
lst = list(map(int, input().split()))

def parametric_search(l, r):
    while r > l:
        mid = (l+r)//2
        if scoreRange(mid) <= M:
            r = mid
        else:
            l = mid+1
    return r

def scoreRange(mid):
    i, res = 0, 1
    _min, _max = INF, -INF
    while i < N:
        _min, _max = min(_min, lst[i]), max(_max,lst[i])
        if _max - _min > mid:
            res += 1
            _min, _max = INF, -INF
        else: i += 1
    return res

print(parametric_search(0, max(lst)))