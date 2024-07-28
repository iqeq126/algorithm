import sys
sys.setrecursionlimit(10**5)
n = int(input())
res = ""
def isGood(length, cur):
    for i in range(1, length // 2 + 1):
        for j in range(0, length - 2 * i + 1):
            if cur[j:j + i] == cur[j + i:j + 2 * i]:
                return False
    return True

def getList(num, cur):
    if n == num:
        res = cur
        print(cur)
        sys.exit(0)
    lst = "123"
    for i in lst:
        if isGood(num+1, cur+i):
            getList(num+1, cur+i)
getList(0, "")