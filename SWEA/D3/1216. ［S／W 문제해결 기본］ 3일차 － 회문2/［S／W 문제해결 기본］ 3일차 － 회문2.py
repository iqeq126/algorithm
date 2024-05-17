# 배열 범위 검증
def is_valid(a):
    return 0 <= a < 100

# 팰린드롬 검사
def is_palindrome(word, res):
    palindrome = word[::-1]
    if word == palindrome:
        return max(res, len(word))
    else:
        return res


for _ in range(1, 11):
    n = int(input())
    res = 0
    board = [list(input()) for _ in range(100)]



    for i in range(100):
        for j in range(100):
            word = []
            for k in range(100):
                if is_valid(j + k):
                    word.append(board[i][j + k])
                else:
                    continue
                res = is_palindrome(word, res)

            word = []
            for k in range(100):
                if is_valid(j + k):
                    word.append(board[j + k][i])
                else:
                    continue
                res = is_palindrome(word, res)

    print(f"#{n} {res}")