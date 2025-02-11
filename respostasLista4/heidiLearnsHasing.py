from math import isqrt

def solve(r):
    for x in range(1, isqrt(r) + 1):
        numerador = r - (x * x + x + 1)
        if numerador > 0 and numerador % (2 * x) == 0:
            y = numerador // (2 * x)
            return f"{x} {y}"
    return "NO"

r = int(input())
print(solve(r))
