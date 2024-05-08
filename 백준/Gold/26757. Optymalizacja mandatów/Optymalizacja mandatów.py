import sys
input = lambda : sys.stdin.readline()
n = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst1.sort()
lst2.sort(reverse=True)
lst2= [ i for _, i in sorted(zip(lst1, lst2) ) ]
res = 0
for i in range(n):
    res += int(f"{lst1[i]}{lst2[i]}")
print(res)