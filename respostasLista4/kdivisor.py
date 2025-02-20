def kth_divisor(n, k):
    divisors = []
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    
    divisors.sort()
    return divisors[k-1] if len(divisors) >= k else -1

n, k = map(int, input().split())
print(kth_divisor(n, k))
