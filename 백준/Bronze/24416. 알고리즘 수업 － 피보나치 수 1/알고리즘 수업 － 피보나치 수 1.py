def fib(n):
    f = [1, 1, 2] + [0] * n
    for i in range(2, n+1):
        f[i+1] = f[i] + f[i-1]
    return f[n-1]
def fibonacci(n):
    return n-2
n = int(input())
print(fib(n), fibonacci(n))