import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
t = int(input())
def termproject():
    def dfs(i, students, visited, cycle):
        visited[i] = True
        cycle.append(i)
        if visited[students[i]]:
            if students[i] in cycle:
                return cycle[cycle.index(students[i]):]
        else:
            return dfs(students[i], students, visited, cycle)

    n = int(input())
    students = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)
    cycle = 0
    for i in range(1, n+1):
        if not visited[i]:
            cycleList = dfs(i, students, visited, [])
            if cycleList:
                cycle += len(cycleList)
    print(n-cycle)
for _ in range(t):
    termproject()