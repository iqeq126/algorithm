import sys
input = sys.stdin.readline
N = int(input())
grapeList =[0,0,0]
lst = [int(input()) for _ in range(N)]
grapeList.extend(lst)
res = [0 for i in range(N+3)]
for i in range(3, N+3):
    graphMax = max(res[i-3] + grapeList[i-1]+grapeList[i], grapeList[i] + res[i-2])
    res[i] = max(graphMax, res[i-1])
print(res[-1])