import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B = [1001 for i in range(N+1)]
ans = 0
for i in range(N):
    if A[i] < B[ans]:
        B[ans+1] = A[i]
        ans += 1
    elif A[i] > B[ans]:
        for j in range(ans+1):
            if A[i] >= B[j]:
                B[j] = A[i]
                break
print(ans)
