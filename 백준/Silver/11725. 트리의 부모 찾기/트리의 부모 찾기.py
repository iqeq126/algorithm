import sys
from collections import deque, defaultdict
input = sys.stdin.readline
def setDict(N):
    dic = defaultdict(list)
    dic[1] = [1]
    for _ in range(N-1):
        x, y = map(int, input().split())
        dic[x].append(y)
        dic[y].append(x)
    return dic
def getParent(N):
    dic = setDict(N)
    q = deque([1])
    parent = defaultdict(int)
    while q:
        cur = q.popleft()
        for i in dic[cur]:
            if parent[i] == 0 and i != 1:
                parent[i] = cur
                q.append(i)
    for _ in range(2, N+1):
        print(parent[_])
getParent(int(input()))