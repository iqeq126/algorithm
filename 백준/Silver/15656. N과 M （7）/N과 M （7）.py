import sys
sys.setrecursionlimit(10**8)
print = sys.stdout.write
n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
def NandM(res):
    if len(res) == m:
        for i in range(m):
            print(f"{res[i]} ")
        print("\n")
        return
    for i in range(n):
        res.append(lst[i])
        NandM(res)
        res.pop()
NandM([])