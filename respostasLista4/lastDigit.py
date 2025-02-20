def last_digit(a, b):
    if b == 0:
        return 1
    last_digit_a = a % 10 
    cycle = [last_digit_a]
    
    while True:
        next_digit = (cycle[-1] * last_digit_a) % 10
        if next_digit == cycle[0]:
            break
        cycle.append(next_digit)
    
    cycle_length = len(cycle)
    index = (b - 1) % cycle_length
    return cycle[index]

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(last_digit(a, b))
