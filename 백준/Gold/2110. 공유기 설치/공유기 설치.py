import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N, C = map(int, input().split())
_list = [int(input()) for i in range(N) ]
_list.sort()
def parameter_search(s, e):
    while e > s:
        mid = (s+e) // 2
        if network_scope(mid) < C:
            e = mid
        else:
            s = mid + 1
    print(e-1)

def network_scope(dis):
    res = 1
    S, E = 0, 0
    while E < N:
        if _list[E] - _list[S] < dis:
            E += 1
        else:
            S = E
            E += 1
            res += 1

    return res
parameter_search(1, _list[-1] - _list[0]+1)