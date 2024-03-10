import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
def is_palindrome(left, right, del_member, S):
    while left < right:
        if S[left] != S[right]:
            if del_member == 0:
                if is_palindrome(left+1, right, 1, S) == 0 or is_palindrome(left, right-1, 1, S) == 0:
                    return 1
            return 2
        else:
            left+=1
            right -=1
    return 0
for _ in range(N):
    S = sys.stdin.readline().rstrip('\n')
    l, r = 0, len(S)-1
    print(is_palindrome(l, r, 0, S))