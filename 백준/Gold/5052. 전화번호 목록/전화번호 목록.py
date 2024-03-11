import sys
input, print = sys.stdin.readline, sys.stdout.write
def is_valid():
    case = int(input())
    phone_book = []
    for _ in range(case):
        phone_book.append(input().rstrip("\n"))
    phone_book.sort()
    for i in range(case-1):
        area_code = len(phone_book[i])
        if phone_book[i+1][:area_code] == phone_book[i]:
            return "NO"
    return "YES"

for _ in range(int(input())):
    print(f"{is_valid()}\n")