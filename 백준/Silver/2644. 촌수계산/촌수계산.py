from collections import deque, defaultdict
N = int(input())
s, e = map(int, input().split())
M = int(input())
q = deque()
dic = defaultdict(list)
visited = defaultdict(bool)
for _ in range(M):
    From, To = map(int, input().split())
    dic[From].append(To)
    dic[To].append(From)
res = -1
q.append([s, 0])
while q:
    now, now_level = q.popleft()
    if now == e:
        res = now_level
        break
    visited[now] = True
    for next in dic[now]:
        if not visited[next]:
            q.append([next, now_level+1])
print(res)