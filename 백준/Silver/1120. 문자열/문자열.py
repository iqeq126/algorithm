import sys
input = sys.stdin.readline
A, B = input().split()
res = len(B)
for i in range(len(B)-len(A)+1):
    local_res = 0
    for j in range(len(A)):
        if A[j] != B[j+i]:
            local_res += 1
    if res > local_res: res = local_res
print(res)