import sys
input = sys.stdin.readline
N, M = map(int, input().split())
sentence = sorted(input().strip() for _ in range(N))
prefix = sorted([input().strip() for _ in range(M)])

res = 0
for pre in prefix:
    left, right = 0, len(sentence) - 1
    while left <= right:
        mid = (left + right) // 2
        if sentence[mid].startswith(pre):
            res += 1
            break
        elif sentence[mid] < pre:
            left = mid + 1
        else:
            right = mid - 1
print(res)