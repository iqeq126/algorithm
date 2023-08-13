import sys
sys.setrecursionlimit(10 ** 8)
input, print= sys.stdin.readline, sys.stdout.write
N = int(input())
K = int(input())
def parametric_search(s,e):
    if s >= e:
        return s
    cnt = 0
    mid = (s + e) // 2
    for i in range(1,N+1):
        cnt += min(mid//i, N)
    if cnt >= K:
        return parametric_search(s, mid)
    else:
        return parametric_search(mid+1, e)
print(str(parametric_search(1, N*N)) + "\n")