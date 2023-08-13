import sys
sys.setrecursionlimit(10**9)
input, print = sys.stdin.readline, sys.stdout.write
N = int(input())
def hanoi(N, _from, _by, _to):
    if N ==1:
        print(str(_from) + " " + str(_to) + "\n")
    elif N <= 20:
        hanoi(N-1, _from, _to, _by)
        print(str(_from) + " " + str(_to) + "\n")
        hanoi(N-1, _by, _from, _to)

def total(t):
    if t > 1:
        return total(t-1) * 2 + 1
    else:
        return 1
print(str(total(N))+"\n")
hanoi(N,1,2,3)