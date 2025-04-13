# Dada uma grade m x n, quantos caminhos existem do canto superior esquerdo até o inferior direito, só podendo mover-se para a direita ou para baixo?

m, n = map(int, input().split())

dp = [[0] * n for _ in range(m)]

for i in range(m):
    dp[i][0] = 1
for j in range(n):
    dp[0][j] = 1

for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 

print(dp[m - 1][n - 1])

