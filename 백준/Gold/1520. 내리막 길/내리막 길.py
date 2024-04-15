import sys, heapq
sys.setrecursionlimit(10 ** 6)
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def getRes():
    q = [(-board[0][0], 0, 0)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1

    while q:
        res, y, x = heapq.heappop(q)
        for i in range(4):
            X, Y = x + dx[i], y + dy[i]
            if 0 <= Y < n and 0 <= X < m:
                if board[y][x] <= board[Y][X]:
                    continue
                if visited[Y][X] == 0:
                    heapq.heappush(q, (-board[Y][X], Y, X))
                visited[Y][X] += visited[y][x]
    return visited[-1][-1]
print(getRes())