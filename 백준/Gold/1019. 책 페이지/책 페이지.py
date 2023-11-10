import sys
input = sys.stdin.readline

book = [0 for _ in range(10)]
def calc(page, state):
    while page > 0:
        book[page % 10] += state
        page //=10

def sol(A, B, state):
    while A%10 != 0 and A <=B:
        calc(A, state)
        A+=1
    if A > B : return
    while B % 10 != 9 and B >= A:
        calc(B, state)
        B -= 1

    cnt = B // 10 - A // 10 + 1
    for i in range(10):
        book[i] += cnt * state
    sol(A//10, B //10, state * 10)

N = int(input())
sol(1,N,1)
print(*book)