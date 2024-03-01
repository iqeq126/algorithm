import sys
input = sys.stdin.readline
N = int(input())
coordinate_plane = sorted([list(map(int, input().split())) for i in range(N)])

def getDist(a, b):
    return getDot(a[0], b[0]) + getDot(a[1], b[1])
def getDot(a, b):
    return (a - b) ** 2

def getMinDist(left, right):
    if left == right: return float('inf')

    if right - left == 1: return getDist(coordinate_plane[left], coordinate_plane[right])

    mid = (left+right)//2
    min_dist = min(getMinDist(left, mid), getMinDist(mid, right))

    boundary = []
    for i in range(left, right+1):
        if getDot(coordinate_plane[mid][0], coordinate_plane[i][0]) < min_dist:
            boundary.append(coordinate_plane[i])

    boundary.sort(key=lambda y:y[1])
    b_len = len(boundary)
    for i in range(b_len-1):
        for j in range(i+1, b_len):
            if getDot(boundary[i][1], boundary[j][1]) < min_dist:
                min_dist = min(min_dist,
                               getDist(boundary[i], boundary[j]))
            else:
                break
    return min_dist
print(getMinDist(0, N-1))