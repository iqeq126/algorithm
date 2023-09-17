s1 = input()
s2 = input()
s1 = "-" + s1
s2 = "-" + s2
LCS = [ [0 for i in range(1002)] for j in range(1002)]
for i in range(len(s1)):
    for j in range(len(s2)):
        if i == 0 or j == 0:
            LCS[0][0] = 0
        elif s1[i] == s2[j]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
print(max(max(LCS)))