# “Você está em um array de números e pode pular até k posições à frente. Qual a maior soma possível até o final?”

entrada = list(map(int, input().split()))
n = len(entrada)
saltos = int(input())

dp = [0] * n
dp[0] = entrada[0]

for i in range(1, n):
    max_anterior = float('-inf')
    for j in range(1, saltos + 1):
        if i - j >= 0:
            max_anterior = max(max_anterior, dp[i - j])
    dp[i] = max_anterior + entrada[i]

print(dp[n - 1])
