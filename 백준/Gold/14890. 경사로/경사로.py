import sys
input = sys.stdin.readline
n,l = map(int, input().split())
ramp = [ list(map(int, input().split())) for _ in range(n) ]

def make_bridge(l, idx):
    return l[idx-1] - l[idx]
def is_ramp(r):
    bridge = [False] * n
    RIGHT, LEFT = 1, -1
    for i in range(1, n):
        if abs(make_bridge(r, i)) > 1:
            return False
        else:
            if make_bridge(r, i) == RIGHT:
                for j in range(l):
                    if i + j >= n or r[i] != r[i+j]:
                        return False
                    if bridge[i+j]:
                        return False
                    bridge[i+j] = True
            elif make_bridge(r, i) == LEFT:
                for j in range(-1, -l-1, -1):
                    if i + j < 0 or r[i-1] != r[i + j]:
                        return False
                    if bridge[i + j]:
                        return False
                    bridge[i + j] = True
    return True

res = 0
for i in range(n):
    if is_ramp(ramp[i]):
        res += 1
    if is_ramp([ramp[j][i] for j in range(n)]):
        res += 1
print(res)