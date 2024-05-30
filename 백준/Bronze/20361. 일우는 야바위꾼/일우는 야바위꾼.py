import sys
input = sys.stdin.readline
n, x, k = map(int, input().split())
lst = [0 for _ in range(n+1)]
lst[x] = 1
for i in range(k):
    a, b = map(int, input().split())
    lst[a], lst[b] = lst[b], lst[a]
print(lst.index(1))