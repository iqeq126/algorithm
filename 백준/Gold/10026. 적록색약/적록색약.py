import sys
sys.setrecursionlimit(10 **9)
input = sys.stdin.readline
N = int(input())
normal = [ list(input().strip('').rstrip('\n')) for i in range(N) ]
abnormal = [ ['' for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if normal[i][j] == "G":
            abnormal[i][j] = "R"
        else:
            abnormal[i][j] = normal[i][j]
rgb = ["R", "G", "B"]
rb = ["R", "B"]
norVisited = [[False for _ in range(N+1)]for _ in range(N+1)]
abVisited = [[False for _ in range(N+1)]for _ in range(N+1)]
norList = [0 for _ in range(700)]
abList = [0 for _ in range(700)]
nIndex = 0
aIndex = 0
X, Y = 0, 0
def dfs(visited,_list, color, x,y, index):
    if not visited[x][y]:
        visited[x][y] = True
        _list[index] +=1
        if y < N-1 and color[x][y] == color[x][y+1]:
            dfs(visited, _list,color, x, y+1, index)
        if y > 0 and color[x][y] == color[x][y-1]:
            dfs(visited, _list,color, x, y-1, index)
        if x > 0 and color[x][y] == color[x-1][y]:
            dfs(visited, _list, color,x-1, y, index)
        if x < N-1 and color[x][y] == color[x+1][y]:
            dfs(visited, _list,color, x+1, y, index)
for i in range(N):
    for j in range(N):
        if norVisited[i][j] == False:
            dfs(norVisited, norList, normal, i, j, nIndex)
            nIndex += 1
for i in range(N):
    for j in range(N):
        if abVisited[i][j] == False:
            dfs(abVisited, abList, abnormal, i, j, aIndex)
            aIndex += 1
norList.sort(reverse=True)
abList.sort(reverse=True)
buf = 0
for i in range(N*N+1):
    if norList[i] == 0:
         buf = i
         break
print(buf, end=" ")
buf = 0
for i in range(N*N+1):
    if abList[i] == 0:
         buf = i
         break
print(buf)