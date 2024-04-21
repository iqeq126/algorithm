n, m = map(int, input().split())
houses, chicken_stores, dists = [], [], []
global min_dist
min_dist = 2501 # 치킨 거리의 최대 크기
city = [[] * n for _ in range(n)]
for i in range(n):
    chicken = list(map(int, input().split()))
    city[i] = chicken
    for j in range(n):
        if chicken[j] == 1:
            houses.append((i, j))
        if chicken[j] == 2:
            chicken_stores.append((i, j))

def get_chicken_dist(y1, x1, y2, x2):
    return abs(y1-y2) + abs(x1-x2)
def get_min_dist(remained_num, closed_num):
    global min_dist
    if remained_num > len(chicken_stores): return
    if closed_num == m:
        dist_sum = 0
        for hy, hx in houses:
            dist = 2501
            for d in dists:
                cy, cx = chicken_stores[d]
                dist = min(dist, get_chicken_dist(hy, hx, cy, cx))
            dist_sum += dist
        min_dist = min(min_dist, dist_sum)
        return
    dists.append(remained_num)
    get_min_dist(remained_num+1, closed_num+1)
    dists.pop()
    get_min_dist(remained_num+1, closed_num)
get_min_dist(0, 0)
print(min_dist)