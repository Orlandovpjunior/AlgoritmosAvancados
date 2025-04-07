n = int(input())
INF = float('inf')
dp = [INF] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for d in str(i):
        dp[i] = min(dp[i], dp[i - int(d)] + 1)

print(dp[n])
