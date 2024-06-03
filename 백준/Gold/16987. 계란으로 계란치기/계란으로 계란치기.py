import sys
n = int(input())
egg = list( list(map(int, input().split())) for _ in range(n))
res = 0 # 최대 계란 개수
def egg_break(idx, cnt):
    global res
    if idx == n:
        res = max(res, cnt)
        return

    if egg[idx][0] <= 0 or cnt == n-1:
        egg_break(idx+1, cnt)
        return

    local_cnt = cnt

    for i in range(n):
        # 본인끼리 박거나, 이미 깨진 경우
        if i == idx or egg[i][0] <= 0:
            continue

        egg_crush(idx, i)

        if egg[idx][0] <= 0:
            cnt += 1

        if egg[i][0] <= 0:
            cnt += 1

        egg_break(idx + 1, cnt)
        # 백트래킹
        egg_recovery(idx, i)
        cnt = local_cnt


def egg_crush(left_egg, right_egg):
    egg[right_egg][0] -= egg[left_egg][1]
    egg[left_egg][0] -= egg[right_egg][1]


def egg_recovery(left_egg, right_egg):
    egg[right_egg][0] += egg[left_egg][1]
    egg[left_egg][0] += egg[right_egg][1]


egg_break(0, 0)
print(res)