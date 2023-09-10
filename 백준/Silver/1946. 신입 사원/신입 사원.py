import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    newFace = [list(map(int, input().split())) for _ in range(N)]
    newFace.sort()
    ans = 0
    buf = newFace[0][1]
    for i in range(N):
        if newFace[i][1] <= buf:
            ans +=1
            buf = newFace[i][1]
    print(ans)