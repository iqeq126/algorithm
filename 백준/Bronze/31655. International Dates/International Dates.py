s = list(map(int, input().split('/')))
if 1 <= s[0] <= 12 and 1 <= s[1] <= 12:
    print("either")
elif 1 <= s[0] <= 12:
    print("US")
elif 1 <= s[1] <= 12:
    print("EU")
else:
    print("either")