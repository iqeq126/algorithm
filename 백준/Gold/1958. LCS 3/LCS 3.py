s1 = input()
s2 = input()
s3 = input()
s1 = "-" + s1
s2 = "-" + s2
s3 = "-" + s3
LCS = [ [[0 for _ in range(102)]for _ in range(102)] for _ in range(102)]
for i in range(len(s1)):
    for j in range(len(s2)):
        for k in range(len(s3)):
            if i == 0 or j == 0 or k == 0:
                LCS[0][0][0] = 0
            elif s1[i] == s2[j] == s3[k]:
                LCS[i][j][k] = LCS[i - 1][j - 1][k-1] + 1
            else:
                LCS[i][j][k] = max(LCS[i - 1][j][k], LCS[i][j - 1][k], LCS[i][j][k-1])
print(max(max(max(LCS))))