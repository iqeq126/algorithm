import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
length, reversed_length = 1,1
res, ans = 1,1
for i in range(1, n):
    if A[i - 1] <= A[i]:
        length += 1
    else:
        length = 1
    if A[i - 1] >= A[i]:
        reversed_length += 1
    else:
        reversed_length = 1
    res = max(length, reversed_length)
    ans = max(ans, res)
print(ans)