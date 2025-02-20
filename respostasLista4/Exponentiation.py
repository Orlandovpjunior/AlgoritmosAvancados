n = int(input())

MOD = 10**9 + 7

def exp(x, y, mod=MOD):
    if y == 0:
        return 1
    res = exp(x, y // 2, mod) 
    res = (res * res) % mod
    if y % 2 != 0:
        res = (res * x) % mod
    return res

for _ in range(n):
    x, y = map(int, input().split())
    print(exp(x, y))
