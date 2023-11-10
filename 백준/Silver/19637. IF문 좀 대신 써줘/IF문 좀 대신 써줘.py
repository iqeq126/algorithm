import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = []
for _ in range(N):
    level, power_range = input().split()
    lst.append([level,int(power_range)])
for _ in range(M):
    player = int(input())
    l,r,mid = 0, N-1, (N-1)//2
    while l <= r:
        mid = (l + r) // 2
        if player <= lst[mid][1]:
            r = mid - 1
        elif player > lst[mid][1]:
            l = mid + 1
    if player > lst[mid][1]:
        print(lst[mid+1][0])
    else:
        print(lst[mid][0])