for t in range(10) :
    n = int(input())
    lst = [ list(map(int, input().split())) for _ in range(n)]
    res, N, S = 0, 1, 2
    for x in range(n):
        status = False
        for y in range(n):
            if lst[y][x] == N :
                status = True
            elif lst[y][x] == S and status:
                res += 1
                status = not status
    print(f"#{t+1} {res}")