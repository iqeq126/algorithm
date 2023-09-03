import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
N = int(input())
_poling = [list(map(int, input().split())) for _ in range(N)]
def poling_222(N, M, C):
    if N == 2:
        subList = [0, 0, 0, 0]
        idx = 0
        for i in range(M, M+2):
            for j in range(C, C+2):
                subList[idx] = _poling[i][j]
                idx += 1
        subList.sort()
        return subList[2]
    else:
        myList = [0, 0, 0, 0]
        N //= 2
        myList[0] = poling_222(N, M, C)
        myList[1] = poling_222(N, M, C+N)
        myList[2] = poling_222(N, M+N, C)
        myList[3] = poling_222(N, M+N, C+N)
        myList.sort()
        return myList[2]
print(poling_222(N,0,0))