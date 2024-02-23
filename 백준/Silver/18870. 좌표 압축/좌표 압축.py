import sys
input, print = sys.stdin.readline, sys.stdout.write
N = int(input())
X = list(map(int ,input().split()))
sortedX = sorted(list(set(X)))
dicX = {sortedX[i] :i for i in range(len(sortedX))}
for i in X:
    print(f"{dicX[i]} ")