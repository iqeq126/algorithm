import copy
n = int(input())
word = list(input().rstrip('\n'))
res = 0
for i in range(n-1):
    copied_word = copy.deepcopy(word)
    next_word = list(input().rstrip('\n'))
    dif = 0
    for nw in next_word:
        if nw in copied_word:
            copied_word.remove(nw)
        else:
            dif += 1
    if dif <= 1 and len(copied_word) <= 1: res+=1
print(res)