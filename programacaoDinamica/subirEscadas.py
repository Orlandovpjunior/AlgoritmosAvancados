n = int(input())

degraus = [1,2]

dp = [0] * (n + 1)
dp[0] = 1

for i in range(n + 1):
    for d in degraus:
        if i - d >= 0:
            dp[i] = dp[i] + dp[i - d]

print(dp[n])


