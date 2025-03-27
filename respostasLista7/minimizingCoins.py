n, x = map(int, input().split())
moedas = list(map(int, input().split()))
inf = float('inf')
dp = [[inf] * (x + 1) for _ in range(n)]

for i in range(x + 1):
    if moedas[0] == 0 or i % moedas[0] != 0:
        dp[0][i] = inf
    else:
        dp[0][i] = i // moedas[0]

for i in range(1, n):
    for j in range(x + 1):
        dp[i][j] = dp[i - 1][j]
        if moedas[i] <= j:
            dp[i][j] = min(dp[i][j], dp[i][j - moedas[i]] + 1)

resposta = dp[n - 1][x]
print(resposta if resposta != inf else -1)
