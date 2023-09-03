import sys
sys.setrecursionlimit(10 ** 9)
moo = "moo"
N = int(input())
def MooGame(n, k, length):
    new_length = length * 2 + k+3
    if n <= 3:
        print(moo[n-1])
        return
    if new_length < n:
        MooGame(n, k+1, new_length)
    else:
        if length < n <= length + k+3:
            if n - length != 1:
                print("o")
            else:
                print("m")
            return
        else:
            MooGame(n - (length + k + 3), 1, 3)
MooGame(N, 1, 3)