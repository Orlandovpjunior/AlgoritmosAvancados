n, x = map(int, input().split())
moedas = list(map(int, input().split()))

INF = float('inf')
dp = [INF] * (x + 1)
dp[0] = 0

for i in range(1, x + 1):
    for m in moedas:
        if i - m >= 0:
            dp[i] = min(dp[i], dp[i - m] + 1)

print(dp[x] if dp[x] != INF else -1)
