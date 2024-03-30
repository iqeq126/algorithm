import math
n = int(input())
a, b, c = n, n+1, -(n+2)
D = b**2 - 4*a*c
if D < 0:
    print(-1)
else:
    d = int(D ** 0.5)
    if d**2 != D:
        print(-1)
    else:
        p1, q1 = -b + d, -b - d
        g1, g2 = math.gcd(p1, 2*a), math.gcd(q1, 2*a)
        p1, q1 = p1 //g1, q1 // g2
        p2, q2 = 2*a // g1, 2*a // g2
        if n % (p2*q2) != 0:
            print(-1)
        else:
            A,B = p2, -p1
            n //= p2
            C, D =n, -q1 * n // q2
            print(A,B,C,D)