import sys
sys.setrecursionlimit(10**8)
print = sys.stdout.write
n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
s = set()
def NandM(res):
    if len(res) == m:
        if tuple(res) not in s:
            for i in range(m):
                print(f"{res[i]} ")
            print("\n")
            s.add(tuple(res))
        return
    for i in range(n):
        res.append(lst[i])
        NandM(res)
        res.pop()
NandM([])