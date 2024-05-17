from collections import defaultdict
for _ in range(10):
    # 번호, 길의 총 개수
    n, E = map(int, input().split())
    node = list(map(int, input().split()))

    # 방문 배열
    visited = [0] * 100
    # 그래프
    graph = defaultdict(list)
    for i in range(E):
        graph[node[i * 2]].append(node[i * 2 + 1])

    def is_visited(n, v):
        # 방문 표시
        visited[v] = 1
        for i in graph[v]:
            # 처음 방문 시에만 방문
            if not visited[i]:
                is_visited(n, i)
        return f"#{n} {visited[99]}"

    print(is_visited(n, 0))