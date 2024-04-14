import sys
from math import ceil, log
sys.setrecursionlimit(10 ** 8)
input, print = sys.stdin.readline, sys.stdout.write

def segment(s, e, i):
    if s == e:
        segTree[i] = ( min_max[s], min_max[s] )
        return segTree[i]
    m = (s + e)//2
    left, right = segment(s, m, i*2 ), segment(m+1, e, i*2+1)
    segTree[i] = ( min( left[0], right[0]), max( left[1], right[1]) )
    return segTree[i]

def query(s, e, i, l, r):
    if l > e or r < s:
        return (1000000000, 0)
    m = (l + r) // 2
    if s <= l and r <= e:
        return segTree[i]
    else:
        left, right = query(s, e, i*2, l, m), query(s, e, i*2+1, m+1, r)
        return ( min( left[0], right[0]), max( left[1], right[1]) )
N, M = map(int, input().split())
# create segment tree
min_max = [0] * N
for _ in range(N):
    min_max[_] = int(input())

H = ceil(log(N, 2)) + 1
treeSize = 1 << H
segTree = [0] * treeSize
segment(0, N-1, 1)

for i in range(M):
    a, b = map(int, input().split())
    ans ,ans2 = query(a-1, b-1, 1,0, N-1)
    print("{} {}\n".format(ans, ans2))