import sys

N, M = map(int, sys.stdin.readline().split())
sentence = sorted(sys.stdin.readline().strip() for _ in range(N))
prefix = [sys.stdin.readline().strip() for _ in range(M)]

def binary_search(sentence, prefix):
    count = 0
    for pre in prefix:
        left, right = 0, len(sentence) - 1
        while left <= right:
            mid = (left + right) // 2
            if sentence[mid].startswith(pre):
                count += 1
                break
            elif sentence[mid] < pre:
                left = mid + 1
            else:
                right = mid - 1
    return count

print(binary_search(sentence, prefix))