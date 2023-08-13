import sys
sys.setrecursionlimit(10 ** 8)
global T, r, c
T = 0
def Z(N, R, C):
    if N == 0:
        return -1
    global T, r, c
    if R == r and C == c:
        print(T)
        return T
    if r < R + N and r >= R and c < C +N and c >= C:
        Z(N // 2, R, C)
        Z(N // 2, R, C + N // 2)
        Z(N // 2, R + N // 2, C)
        Z(N // 2, R + N // 2, C + N // 2)
    else:
        T += N * N

input = sys.stdin.readline
N, r, c = map(int, input().split())
Z(4 ** N, 0, 0)
