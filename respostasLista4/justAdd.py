import sys

MOD = 10000007

def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def sum_of_powers(k, n, mod):
    if k == 1:
        return n % mod
    num = (mod_exp(k, n, mod) - 1 + mod) % mod  # (k^n - 1) % mod
    den = mod_exp(k - 1, mod - 2, mod)  # Modular inverse of (k-1) using Fermat's theorem
    return (num * den) % mod

def compute_zn(n, k):
    s_n = sum_of_powers(k, n, MOD)
    p_n = sum_of_powers(n, n, MOD)
    return (s_n + p_n) % MOD

def solve(n, k):
    if n < 2:
        return 0
    z_n = compute_zn(n, k)
    z_n_1 = compute_zn(n - 1, k)
    z_n_2 = compute_zn(n - 2, k)
    return (z_n + z_n_1 - 2 * z_n_2) % MOD

def main():
    input_data = sys.stdin.read().strip().split("\n")
    for line in input_data:
        n, k = map(int, line.split())
        if n == 0 and k == 0:
            break
        print(solve(n, k))

if __name__ == "__main__":
    main()
