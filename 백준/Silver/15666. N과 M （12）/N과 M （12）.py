import sys
sys.setrecursionlimit(10**8)
print = sys.stdout.write
n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
def NandM(s, res):
    if len(res) == m:
        for i in range(m):
            print(f"{res[i]} ")
        print("\n")
        return
    buf = 0
    for i in range(s, n):
        if buf != lst[i]:
            res.append(lst[i])
            buf = lst[i]
            NandM(i, res)
            res.pop()
NandM(0, [])