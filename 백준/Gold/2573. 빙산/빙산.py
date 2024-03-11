from collections import deque
import sys
input = sys.stdin.readline
dxy = [[1,0], [-1,0], [0,1], [0,-1]]

CONNECTED_COMPONENT = 1
NOT_SEPERATED = 0
time = 0
tag = False

def melting_ices(time, tag):
    N, M = map(int, input().split())
    sea = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    water_count = [[0] * M for _ in range(N)]

    def is_connected(i, j):
        q = deque()
        q.append([i, j])
        while q:
            cur_x, cur_y = q.popleft()
            visited[cur_x][cur_y] = True
            for dx, dy in dxy:
                near_x, near_y = cur_x + dx, cur_y + dy
                if 0<= near_x < N and 0 <= near_y < M:
                    if sea[near_x][near_y] > 0 and visited[near_x][near_y] == False:
                        visited[near_x][near_y] = True
                        q.append([near_x, near_y])
                    elif sea[near_x][near_y] == 0:
                        water_count[cur_x][cur_y] += 1


        return CONNECTED_COMPONENT

    while True:
        visited = [[False for _ in range(M)] for _ in range(N)]
        water_count = [[0] * M for _ in range(N)]
        connected_ices = []
        for i in range(N):
            for j in range(M):
                if sea[i][j] != 0 and visited[i][j] == False:
                    connected_ices.append(is_connected(i, j))

        for i in range(N):
            for j in range(M):
                sea[i][j] -= water_count[i][j]
                if sea[i][j] < 0: sea[i][j] = 0

        if not connected_ices: break
        if len(connected_ices) > 1:
            tag = True
            break
        time += 1

    if tag: return time
    else: return NOT_SEPERATED

print(melting_ices(time, tag))