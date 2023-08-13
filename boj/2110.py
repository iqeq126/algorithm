import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N, C = int(input().split())
_list = [int(input()) for i in range(N) ]
_list.sort()
def parameter_search(s, e):
    if s > e:
        return s

parameter_search(1, _list[-1])