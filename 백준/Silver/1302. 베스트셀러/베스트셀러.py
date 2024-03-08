from collections import Counter
N = int(input())
best_seller = sorted([ input().rstrip() for _ in range(N)])
print(Counter(best_seller).most_common(1)[0][0])