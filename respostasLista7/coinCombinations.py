n, x = map(int, input().split())

moedas = list(map(int, input().split()))
MOD = 10**9 + 7
INF = float('inf')
dp = [0] * (x + 1)
dp[0] = 1

for i in range(1, x + 1):
    for coin in moedas:
        if coin <= i:
            dp[i] = (dp[i] + dp[i - coin] % MOD)

print(dp[x])