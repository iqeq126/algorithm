import sys
input = sys.stdin.readline
N, K = map(int, input().split())
_list = []
for i in range(N):
    t = int(input())
    _list.append(t)
_list.sort()
DP = [ 0 for i in range(K+1)]
DP[0] = 1
for i in range(1, N+1):
    for j in range(_list[i-1], K+1):
        DP[j] += DP[j - _list[i-1]]

print(DP[K])
