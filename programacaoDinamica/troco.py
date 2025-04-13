# roblema: "De quantas formas posso dar troco de n usando moedas de 1, 2 e 5?"

n = int(input())

moedas = [1,2,5]

dp = [0] * (n + 1)
dp[0] = 1

for m in moedas:
    for i in range(m, n + 1):
        dp[i] += dp[i - m]

print(dp[n])
