import sys
S = sys.stdin.readline().rstrip("\n") # 문자열 입력
L = len(S) # 문자열 길이
dp = [2500 for _ in range(L+1)] # dp 배열 정의(max값 2500)
dp[-1] = 0  # dp[1,1,1,1] : dp[3] == dp[-1]
# 1자리인 펠린드롬 : 인덱스가 같은 경우 True, 나머지 False. (문자 하나는 그 자체로 펠린드롬이기에)
is_palindrome = [[True if _ == __ else False for _ in range(L)] for __ in range(L)]

# 2자리인 펠린드롬 : AA, BB와 같은 형태의 펠린드롬인 경우
for i in range(1, L):
    if S[i - 1] == S[i]: is_palindrome[i - 1][i] = True

# 3자리 이상인 펠린드롬
for l in range(3, L + 1):
    for s in range(L - l + 1):
        e = s + l - 1
        # S[s] == S[e]인 경우는 ex) abcba. S[0] == S[4], S[1] == S[3] , ...
        # 마찬가지로. is_palindrome[s+1][e-1]. 즉, 위에서 보면? S[1] == S[3]
        if S[s] == S[e] and is_palindrome[s + 1][e - 1]: is_palindrome[s][e] = True

for e in range(L): # 0 ~ L-1
    for s in range(e + 1): # 0 ~ e
        # dp[e] = min(dp[e], dp[s - 1] + 1) if is_palindrome[s][e] else min(dp[e], dp[e - 1] + 1)
        # 기존의 dp[e] vs dp[s-1] or dp[e-1]에 저장된 놈 + 1
        #
        if is_palindrome[s][e]:
            dp[e] = min(dp[e], dp[s - 1] + 1)
        #else:
        #    dp[e] = min(dp[e], dp[e - 1] + 1)
print(dp[L-1])