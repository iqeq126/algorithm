n, k = map(int, input().split())
def move_water(water):
    cnt = 0
    while water:
        if water % 2:
            cnt += 1
        water //= 2
    return cnt

def get_result(n, k):
    result = 0
    if n <= k: print(0)
    else:
        while True:
            res = move_water(n)
            if res <= k:
                print(result)
                return
            result += 1
            n += 1
get_result(n, k)