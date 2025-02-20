MOD = 10**9 + 7

def count_valid_arrays(n, l, r):
    count = [0, 0, 0]
    
    count[0] = (r // 3) - ((l - 1) // 3)
    count[1] = ((r + 2) // 3) - ((l + 1) // 3)
    count[2] = ((r + 1) // 3) - (l // 3)

    dp = [0] * 3
    dp[0] = count[0]
    dp[1] = count[1]
    dp[2] = count[2]

    for _ in range(n - 1):
        new_dp = [0] * 3
        new_dp[0] = (dp[0] * count[0] + dp[1] * count[2] + dp[2] * count[1]) % MOD
        new_dp[1] = (dp[0] * count[1] + dp[1] * count[0] + dp[2] * count[2]) % MOD
        new_dp[2] = (dp[0] * count[2] + dp[1] * count[1] + dp[2] * count[0]) % MOD
        dp = new_dp

    return dp[0]

n, l, r = map(int, input().split())

print(count_valid_arrays(n, l, r))
