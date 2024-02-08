import sys
input = sys.stdin.readline
def alphaCentauri(x, y):
    res, k, dist = 0, 1, y-x
    if dist < 4:
        res = dist
    else:
        while True:
            dist -= 2*k
            k+=1
            if dist == 0:
                res= 2*k - 2
                break
            elif 0 < dist <= k:
                res= 2*k-1
                break
            elif k < dist < 2*k:
                res= 2*k
                break
    print(res)
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    alphaCentauri(x,y)
