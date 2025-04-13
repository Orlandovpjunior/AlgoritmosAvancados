s = input()
n = len(s)

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for tamanho in range(2, n + 1):
    for i in range(n - tamanho + 1):
        j = i + tamanho - 1

        if s[i] == s[j]:
            if tamanho == 2:
                dp[i][j] = 2
        else:
            dp[i][j] = dp[i + 1][j-1] + 2
    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])



