import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B = [i for _, i in sorted(zip(A, B))]
A.sort()
AB = []
res = m
for i in range(n):
    if A[i] - B[i] < 0:
        AB.append([A[i], B[i]])
for j in range(len(AB)):
    if res - AB[j][0] > 0:
        res = res - AB[j][0] + AB[j][1]
print(res)