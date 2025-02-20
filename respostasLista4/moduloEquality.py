from collections import Counter

def find_minimum_x(n, m, a, b):
    a.sort()
    b.sort()
    
    b_counts = Counter(b)
    min_x = float('inf')

    for i in range(n):
        x = (b[0] - a[i]) % m
        modified_a = sorted((ai + x) % m for ai in a)
        
        if Counter(modified_a) == b_counts:
            min_x = min(min_x, x)
    
    return min_x

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(find_minimum_x(n, m, a, b))
