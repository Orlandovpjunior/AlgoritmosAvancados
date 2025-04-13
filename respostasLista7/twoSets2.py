n = int(input())
MOD = 10**9 + 7

total = n * (n + 1) // 2

if total % 2 != 0:
    print(0)
else:
    target = total // 2

    dp = [0] * (target + 1)
    dp[0] = 1

    for num in range(1, n + 1):
        for s in range(target, num - 1, -1):
            dp[s] = (dp[s] + dp[s - num]) % MOD

    inv_2 = pow(2, MOD - 2, MOD) 
    print((dp[target] * inv_2) % MOD)
