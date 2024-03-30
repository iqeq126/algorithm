import sys
input = sys.stdin.readline
n, m = map(int, input().split())
shelve = sorted(list(map(int, input().split())), key=lambda x: -abs(x))
pos, neg, res = [], [], -abs(shelve[0])
for book in shelve:
    pos.append(book) if book >= 0 else neg.append(-book)
for i in range(0, len(pos), m):
    res += pos[i]*2
for i in range(0, len(neg), m):
    res += neg[i]*2
print(res)