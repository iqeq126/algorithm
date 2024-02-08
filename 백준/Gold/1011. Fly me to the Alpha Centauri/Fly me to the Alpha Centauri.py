import sys
input = sys.stdin.readline
def alphaCentauri(x, y):
    k, dist = 1, y-x
    if dist < 4:
        return dist
    else:
        while True:
            dist -= 2*k
            k+=1
            if dist == 0: return 2*k - 2
            elif 0 < dist <= k: return 2*k-1
            elif k < dist < 2*k: return 2*k
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(alphaCentauri(x,y))