n, k = map(int, input().split())
alturas = list(map(int,input().split()))

inf = float('inf')
dp = [inf] * n
dp[0] = 0

for i in range(1, n):
    for j in range(1, k + 1):
        if i - j >= 0:
            custo = abs(alturas[i] - alturas[i - j])
            dp[i] = min(dp[i], dp[i - j] + custo)
print(dp[n - 1])