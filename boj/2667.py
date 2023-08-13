import sys
from collections import defaultdict, deque
input = sys.stdin.readline
N = int(input())
S = [ list(map(int, input().strip('').rstrip('\n'))) for i in range(N) ]
visited = [[False for _ in range(N+1)]for _ in range(N+1)]
graph = defaultdict(list)
for i in range(N):
    for j in range(N):
        if S[i][j] == 1:
            graph[i].append(j)
# print(graph)
ans_list = [0] * 700
global index
index = 0
X, Y = 0, 0
def dfs(x,y):
    # print(ans_list[index], x, y)
    if not visited[x][y] and S[x][y] == 1:
        visited[x][y] = True
        ans_list[index] +=1
        if y < N-1:
            dfs(x, y+1)
        if y > 0:
            dfs(x, y-1)
        if x > 0:
            dfs(x-1, y)
        if x < N-1:
            dfs(x+1, y)
for i in range(N):
    for j in range(N):
        if visited[i][j] == False and S[i][j] == 1:
            dfs(i, j)
        index += 1
ans_list.sort(reverse=True)
buf = 0
for i in range(N*N+1):
    if ans_list[i] == 0:
         buf = i
         break
print(buf)
if buf != 0:
    print(*ans_list[buf-1::-1], sep="\n")
else:
    print(0)
"""
h_list = []
Q = deque([])
def bfs(x):
    Q = deque([x])
    cnt = 0
    while Q:
        v = Q.popleft()
        print(v, sep=" ")
        for v in range(N):
            for i in graph[v]:
                if not visited[v][i]:
                    buf = i
                    Q.append(i)
                    visited[v][i] = True
                    cnt += 1
                    if buf > i

        h_list.append(cnt)

for i in range(N*N+1):
    bfs(0)
h_list.sort()
print(len(h_list))
print(*h_list[:], sep='\n')
"""