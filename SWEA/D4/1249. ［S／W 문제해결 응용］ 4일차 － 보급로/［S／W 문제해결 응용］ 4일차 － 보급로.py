import heapq
x = [0, 1, 0, -1]
y = [1, 0, -1, 0]
Test = int(input())
for k in range(Test):
    N = int(input())
    lst = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        line = input().strip("\n")
        for j in range(N):
            lst[i][j] = int(line[j])
    result = [[99999999999999999999999999999 for _ in range(N)] for _ in range(N)]
    Q = []
    heapq.heappush(Q, [0,0])
    result[0][0] = lst[0][0]
    while Q:
        ix, iy = heapq.heappop(Q)
        if result[ix][iy] < lst[ix][iy]:
            continue

        for idx in range(4):
            X, Y = ix + x[idx], iy + y[idx]
            if (0<= X < N) and (0 <= Y < N):
                if result[X][Y] > result[ix][iy] + lst[X][Y]:
                    result[X][Y]= result[ix][iy] + lst[X][Y]
                    Q.append([X, Y])
    print(f"#{k+1} {result[N-1][N-1]}")


