# Dado um conjunto de inteiros positivos e um valor S, existe uma combinação que soma exatamente S?

nums = list(map(int, input().split()))
alvo = int(input())

dp = [False] * (alvo + 1)
dp[0] = True

for i in range(1, alvo + 1):
    for n in nums:
        if i - n >= 0 and dp[i - n]:
            dp[i] = True

print(dp[alvo])



