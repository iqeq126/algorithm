from collections import deque
N, K = map(int, input().split())
length = N-K
lst = list(input())
res = deque()
for i in range(N):
    while len(res) and ( res[-1] < lst[i] ):
        if not K: break
        res.pop()
        K-= 1
    res.append(lst[i])
for i in range(length):
    print(res.popleft(), end="")