import sys
input = sys.stdin.readline
dx =[1, 0, -1, 0]
dy =[0, -1, 0, 1]
N = int(input())
dragon_curve = [list(map(int, input().split())) for _ in range(N)]
graph = [[0] * 101 for _ in range(101)]
for cur_x, cur_y, d, g in dragon_curve:
    graph[cur_y][cur_x] = 1
    route_d = [d]
    next_x, next_y = cur_x + dx[d], cur_y + dy[d]
    graph[next_y][next_x] = 1
    for i in range(g):
        length_d = len(route_d)
        cur_route_d = route_d[:]
        for j in range(1, length_d+1):
            cur_d = cur_route_d[-1*j] + 1
            if cur_d > 3: cur_d = 0
            next_x, next_y = next_x + dx[cur_d] , next_y + dy[cur_d]
            if 0<= next_x <= 100 and 0 <= next_y <= 100:
                graph[next_y][next_x] = 1
                route_d.append(cur_d)

res = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] == graph[i][j+1] == graph[i+1][j] == graph[i+1][j+1] == 1:
            res += 1
print(res)