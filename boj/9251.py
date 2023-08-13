# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence
s1 = input()
s2 = input()
s1 = "-" + s1
s2 = "-" + s2
answer = []
LCS = [ [0 for i in range(1002)] for j in range(1002)]
for i in range(len(s1)):
    for j in range(len(s2)):
        if i == 0 or j == 0:
            LCS[0][0] = 0
        elif s1[i] == s2[j]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
