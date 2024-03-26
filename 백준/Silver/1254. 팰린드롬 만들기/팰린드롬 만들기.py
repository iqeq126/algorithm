s = list(input())
def get_palindrome_size(s):
    for i in range(len(s)):
        sub_s = s[i:]
        if sub_s[:] == sub_s[::-1]:
            return 2 * len(s) - len(sub_s)
print(get_palindrome_size(s))