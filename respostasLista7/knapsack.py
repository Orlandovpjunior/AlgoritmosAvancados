S, N = map(int, input().split()) 
tamanho = []
valor = []

for _ in range(N):
    w, v = map(int, input().split())
    tamanho.append(w)
    valor.append(v)

dp = [0] * (S + 1)

for i in range(N):
    for j in range(S, tamanho[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - tamanho[i]] + valor[i])

print(dp[S])
