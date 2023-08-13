import sys
input = sys.stdin.readline
N = int(input())
answer = 0
A = list(map(int, input().split()))
B, C = set(), set()
A.sort(key=abs)
buf = "A"
for i in range(N):
    for j in range(i+1, N):
        I, J = A[i], A[j]
        if I + J == I or I + J == J:
            size = len(C)
            C.add(I + J)
            if len(C) > size:
                buf = j
            elif len(C) == size and buf == j:
                pass
            else:
                B.add(I +  J)
        else:
            B.add(I + J)
for i in range(N):
    if A[i] in B:
        answer += 1
print(answer)