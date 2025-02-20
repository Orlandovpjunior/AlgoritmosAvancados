def longest_divisors_interval(n):
    l = 1
    while n % (l + 1) == 0:
        l += 1
    return l

t = int(input())
for _ in range(t):
    n = int(input())
    print(longest_divisors_interval(n))
