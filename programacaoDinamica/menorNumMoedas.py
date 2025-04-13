# Você tem moedas de valores [1, 3, 4]. Qual o menor número de moedas para fazer o troco de n?

n = int(input())

moedas = [1, 3, 4]

dp = [float('inf')] * (n + 1)
dp[0] = 0 

for i in range(1, n + 1):
    for m in moedas:
        if i - m >= 0:
            dp[i] = min(dp[i], dp[i - m] + 1)

print(dp[n])
