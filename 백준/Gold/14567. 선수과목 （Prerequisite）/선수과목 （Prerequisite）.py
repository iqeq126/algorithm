import sys
from collections import deque, defaultdict
input, print = sys.stdin.readline, sys.stdout.write
n, m = map(int, input().split())
module = defaultdict(list) # 모듈(과목)
dependency_list = [0] * (n+1) # 의존성 리스트
semester = [1] * (n+1) # 학기
q = deque()
for i in range(m):
    a, b = map(int, input().split())
    module[a].append(b)
    dependency_list[b] += 1

for i in range(1, n+1):
    if not dependency_list[i]:
        q.append(i)
    else:
        semester[i] = 0

while q:
    dependency = q.popleft()
    for process in module[dependency]:
        dependency_list[process] -= 1
        semester[process] = semester[dependency] + 1
        if not dependency_list[process]:
            q.append(process)

for i in range(1, n):
    print(f"{semester[i]} ")
print(f"{semester[n]}\n")