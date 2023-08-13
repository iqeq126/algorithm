import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N, M = map(int, input().split())
_list = list(map(int, input().split()))
_list.sort()
def parametical_search(s, e):
    if s > e:
        return s-1
    cnt = 0
    mid = (s + e) // 2
    for i in range(N):
        if _list[i] >= mid:
            cnt += ( _list[i] - mid )
    if cnt >= M:
        return parametical_search(mid+1, e)
    else:
        return parametical_search(s, mid-1)
print(parametical_search(1, _list[-1]))