import sys
def is_valid():
    case = int(input())
    phone_book = []
    for _ in range(case):
        phone_book.append(sys.stdin.readline().rstrip("\n"))
    phone_book.sort()
    for i in range(case-1):
        area_code = len(phone_book[i])
        if phone_book[i+1][:area_code] == phone_book[i]:
            return "NO"
    return "YES"


for _ in range(int(sys.stdin.readline())):
    print(is_valid())