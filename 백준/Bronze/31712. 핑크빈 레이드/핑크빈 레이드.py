cu, du = map(int, input().split())
cd, dd = map(int, input().split())
cp, dp = map(int, input().split())
hp = int(input())
if hp <= du + dd + dp:
    print(0)
else:
    t = 1
    hp = hp - du - dd - dp
    while hp > 0:
        if t % cu== 0:
            hp -= du
        if t % cd == 0:
            hp -= dd
        if t %cp == 0:
            hp -= dp
        t += 1
    print(t-1)