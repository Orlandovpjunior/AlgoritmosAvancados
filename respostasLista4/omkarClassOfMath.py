from math import sqrt

def solve():
    n = int(input())

    if n % 2 == 0:
        print(n // 2, n // 2)
        return

    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            print(n // i, n - (n // i))
            return
    print(1, n - 1)

t = int(input())
for _ in range(t):
    solve()
