import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
class DisjointSet:
    def __init__(self, n):
        self.data = list(range(n))
        self.size = n
    def find(self, index):
        if index == parent[index]: return index
        parent[index] = self.find(parent[index])
        return parent[index]
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x > y:
            parent[x] = y
            return
        else:
            parent[y] = x

N, M = map(int, input().split())
parent = [_ for _ in range(N)]
disjoint = DisjointSet(N)
for _ in range(M):
    a, b = map(int, input().split())
    if disjoint.find(a) == disjoint.find(b):
        print(_+1)
        break
    disjoint.union(a,b)
else:
    print(0)