import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
N_list.sort()

def parametric_search(s, e):
    if s > e:
        return s-1
    cnt = 0
    mid = (s + e) // 2
    for i in range(N):
        if N_list[i] < mid:
            cnt += (N_list[i])
        else:
            cnt += mid
    if cnt <= M:
        return parametric_search(mid+1, e)
    else:
        return parametric_search(s, mid-1)
print(parametric_search(1, N_list[-1]))