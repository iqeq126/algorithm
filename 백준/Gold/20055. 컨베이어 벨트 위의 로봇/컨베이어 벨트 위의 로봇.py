from collections import deque
n,k = map(int, input().split())
conveyor_belt = deque()
conveyor_belt.extend(list(map(int, input().split())))
belt = 0
def conveyor_belt_on_the_robots(n, k, conveyor_belt):
    robots = deque()
    robots.extend([False] * n)
    res, now = 0, n-2
    while conveyor_belt.count(0) < k:
        res += 1
        conveyor_belt.rotate(1); robots.rotate(1)

        robots[n - 1] = False

        for now in range(n-2, -1, -1):
            next = now+1
            if robots[now] and not robots[next] and conveyor_belt[next] != 0:
                robots[now], robots[next] = False, True
                conveyor_belt[next] -= 1

        robots[n - 1] = False

        if conveyor_belt[0] > 0:
            robots[0] = True
            conveyor_belt[0] -= 1

    return res

print(conveyor_belt_on_the_robots(n, k, conveyor_belt))