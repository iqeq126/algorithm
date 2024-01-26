import sys
from collections import deque
input = sys.stdin.readline
# 사람 수 N, 파티수 M
N, M = map(int, input().split())
people = [0 for _ in range(N+2)]
truth = deque(map(int, input().split()))
truth.popleft()


parties = []
for i in range(M):
    party = deque(map(int, input().split()))
    party.popleft()
    parties.append(party)


for _ in range(N):
    for i in range(M):
        party = parties[i]
        if set(party) & set(truth):
            truth = deque(set(truth) | set(party))

for t in truth:
    people[t] = -1

if not truth:
    print(M)
else:
    res = 0
    #포함되는 모임 제외
    for i in range(M):
        for t in truth:
            if t in parties[i]:
                for p in parties[i]:
                    people[p] = -1
                break
    for i in range(M):
        tag = 1
        for p in parties[i]:
            if people[p] == -1:
                tag = 0
        res += tag
    print(res)