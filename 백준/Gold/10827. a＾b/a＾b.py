from decimal import Decimal, getcontext
a, b = input().split()
getcontext().prec = 1111
print(f"{Decimal(a)**int(b):f}")