N = int(input())

def star(n):
    for i in range(n):
        for j in range(n-i-1):
            print("_", end="")
        for j in range(i+1):
            print("*", end="")
        for j in range(n-i-1):
            print("_", end="")
        for j in range(i+1):
            print("*", end="")
        for j in range(n-i):
            print("_", end="")
        print()

star(N)
