import sys
S = sys.stdin.readline().rstrip("\n")
L = len(S)
dp = [2500 for _ in range(L+1)]
dp[-1] = 0
is_palindrome = [[True if _ == __ else False for _ in range(L)] for __ in range(L)]

for i in range(1, L):
    if S[i - 1] == S[i]: is_palindrome[i - 1][i] = True

for l in range(3, L + 1):
    for s in range(L - l + 1):
        e = s + l - 1
        if S[s] == S[e] and is_palindrome[s + 1][e - 1]: is_palindrome[s][e] = True

for e in range(L):
    for s in range(e + 1):
        dp[e] = min(dp[e], dp[s - 1] + 1) if is_palindrome[s][e] else min(dp[e], dp[e - 1] + 1)
print(dp[L-1])