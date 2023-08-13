import sys
sys.setrecursionlimit(10**7)
input, _list = sys.stdin.readline, []
N, K = map(int, input().split())
for i in range(N):
    t = int(input())
    _list.append(t)
_list.sort()
def parametical_search(s, e):
    if s <= e:
        cnt = 0
        mid = (s + e) // 2
        for i in range(N):
            cnt += ( _list[i] // mid )
        if cnt >= K:
            return parametical_search(mid+1, e)
        else:
            return parametical_search(s, mid-1)
    return e
print(parametical_search(1, _list[-1]))