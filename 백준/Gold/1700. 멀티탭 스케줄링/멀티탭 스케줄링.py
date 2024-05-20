import sys
input = sys.stdin.readline
n, k = map(int, input().split())
sequence = list(map(int, input().split()))
multi_tap = [-1] * n
res = 0
cnt, out = 0, 0
while sequence:
    App = sequence[0]
    if App in multi_tap:
        sequence.remove(App)
        continue

    if multi_tap.count(-1):
        multi_tap[multi_tap.index(-1)] = App
        sequence.remove(App)
        continue

    cnt = -1
    out = 0
    for tap in multi_tap:
        if tap not in sequence:
            out = tap
            break

        elif sequence.index(tap) > cnt:
            cnt = sequence.index(tap)
            out = tap

    multi_tap[multi_tap.index(out)] = App
    sequence.remove(App)
    cnt = -1
    res += 1
print(res)