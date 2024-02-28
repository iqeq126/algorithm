import sys
input = sys.stdin.readline
N = int(input())
res = 0
lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
alpha = [0 for _ in range(26) ]
words = [list(input().rstrip()) for _ in range(N)]
for word in words:
    word_length, i = len(word), 0
    for w in range(word_length):
        alpha[ ord(word[w]) - 65 ] += 10 ** (word_length - w-1)
        i += 1

alpha.sort(reverse=True)
res, i = 0, 0
while alpha[i] > 0:
    res += alpha[i] * lst[i]
    i+=1
print(res)