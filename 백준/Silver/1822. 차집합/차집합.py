import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = set(map(int, input().split()))
B = list(map(int, input().split()))
for b in B:
    if b in A:
        A.remove(b)
print(len(A))
if len(A):
    print(*sorted(list(A)))