import sys
N = int(sys.stdin.readline())
S = list(map(int,sys.stdin.readline().split()))
L = [0] * 2000000
L[0] = 1
subsets = [[]]
for i in range(N):
    L[S[i]] = 1
for i in S:
    size = len(subsets)
    for j in range(size):
        subsets.append(subsets[j] + [i])
        L[sum(subsets[j] + [i])] = 1
print(L.index(0))