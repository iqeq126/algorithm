import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
cheeze = [[0 for i in range(M)]for j in range(N)]
_list = [list(map(int, input().split())) for _ in range(N)]
q = deque()
q.append([0,0])
def bfs():
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]