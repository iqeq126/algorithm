import sys
from math import ceil, log
sys.setrecursionlimit(10 ** 8)
input, print = sys.stdin.readline, sys.stdout.write

def segment(l, r, i):
    if l == r:
        segTree[i] = _list[l]
        return segTree[i]
    m = (r + l)//2
    segTree[i] = segment(l, m, i*2) + segment(m+1, r, i*2+1)
    return segTree[i]

def query(s, e, i, l, r):
    if l > e or r < s:
        return 0
    if s >= l and r >= e:
        return segTree[i]
    m = (s + e) // 2
    return query(s, m, i*2, l, r) + query(m+1, e, i*2+1, l, r)

def update(s, e, node, i, val):
    if s > i or i > e:
        return segTree[node]
    segTree[node] += val
    if s != e:
        m = (s + e)// 2
        update(s, m, node*2, i, val)
        update(m+1, e, node*2 + 1, i, val)

N, M, K = map(int, input().split())
# create segment tree
_list = []
for _ in range(N):
    t = int(input())
    _list.append(t)

H =ceil(log(N, 2)+1)
treeSize = pow(2, H+1)
segTree = [0] + [0] * treeSize
segment(0, N-1, 1)
for _ in range(K+M):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        dif_num = c - _list[b]
        _list[b] = c
        update(0, N-1, 1, b, dif_num)
        #K -= 1
    elif a == 2:
        print(f"{query(0, N-1, 1, b-1, c-1)}\n")
        #M -= 1
