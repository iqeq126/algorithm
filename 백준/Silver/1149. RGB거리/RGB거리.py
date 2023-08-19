import sys
input = sys.stdin.readline
N = int(input())
R, G, B = [0 for i in range(N)], [0 for i in range(N)], [0 for i in range(N)]
for i in range(N):
    R[i], G[i], B[i] = map(int, input().split())
if N == 1:
    print(min(R[0], G[0], B[0]))
else:
    for i in range(1, N):
        R[i] = R[i] + min(G[i-1], B[i-1])
        G[i] = G[i] + min(R[i-1], B[i-1])
        B[i] = B[i] + min(R[i-1], G[i-1])

    print(min(R[N-1],G[N-1], B[N-1]))