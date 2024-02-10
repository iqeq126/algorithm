import sys
input = sys.stdin.readline
N = int(input())
N_lst = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
M_lst = sorted(list(map(int, input().split())), reverse=True)
res = 0
if N_lst[0] < M_lst[0]:
    res = -1
else:
    while M_lst:
        for n in N_lst:
            for m in M_lst:
                if n >= m:
                    M_lst.remove(m)
                    break
        res+=1
print(res)