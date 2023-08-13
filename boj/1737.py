import sys
PI = 3.14159265359
t = 1000000000000000000
P = [1 for i in range(1006)]
n = int(sys.stdin.readline())
P[4] = 2
for i in range(4, 1005):
    if i > int(2*PI)+1:
        P[int(i - PI)] = ((P[int(i-1 - PI)] %t + P[(int(i - 2 * PI))] %t)) % t
    P[i] = (P[i-1] % t + P[int(i-PI)] % t) % t
print(P[n])