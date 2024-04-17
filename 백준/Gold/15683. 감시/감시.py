import sys
from copy import deepcopy
input = sys.stdin.readline
search_lst = []
# 방향 지정
direction = [[-1, 0], [1, 0], [0,-1], [0,1]] # bottom, top, left, right
cctv = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 2], [0, 3], [1, 2], [1, 3]],
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    [[0, 1, 2, 3]]
]
visited, void, wall = -1, 0, 6 # 빈 칸, 벽
global result # 최대 크기
result = 81
height, width = map(int, input().split())
# 사무실 그래프
office = [list(map(int, input().split())) for _ in range(height)]

for i in range(height):
    for j in range(width):
        if void < office[i][j] < wall:
            search_lst.append((i,j, office[i][j]))

def dfs(office, depth):
    global result
    if depth == len(search_lst):
        local_res = 0
        for i in range(height):
            local_res += office[i].count(0)
        result = min(result, local_res)

    else:
        copied_office = deepcopy(office)
        y, x, now = search_lst[depth]
        for now_cctv in cctv[now]:
            for c in now_cctv:
                ny, nx = y, x
                while True:
                    ny, nx = ny + direction[c][0], nx + direction[c][1]
                    if 0 <= ny < height and 0 <= nx < width:
                        if copied_office[ny][nx] == wall:
                            break
                        elif copied_office[ny][nx] == void:
                            copied_office[ny][nx] = visited
                    else:
                        break
            dfs(copied_office, depth+1)
            copied_office = deepcopy(office)

dfs(office, 0)
print(result)