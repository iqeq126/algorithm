import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
I = -1
for i in range(N):
    flag = 0
    for j in range(N-1) :
        if A[j] > A[j+1]:
            flag = 1
            A[j], A[j+1] = A[j+1], A[j]
    if flag == 0:
        I = i
        break
print(I)