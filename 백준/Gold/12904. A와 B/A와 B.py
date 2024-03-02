S = list(input())
T = list(input())
def AB(S, T):
    while len(S) < len(T):
        if T.pop() == 'B':
            T = T[::-1]
    print(1) if S==T else print(0)
AB(S,T)