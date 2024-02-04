import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
lst.sort()
res = sys.maxsize
one, two, three = 0,0,0
for first in range(len(lst)-1):
    second, third = first+1, len(lst)-1
    while second < third:
        water = lst[first] + lst[second] + lst[third]
        if abs(water) < res:
            res = abs(water)
            one, two, three = lst[first], lst[second], lst[third]
        if water < 0: second += 1
        else: third -= 1
print(one, two, three)