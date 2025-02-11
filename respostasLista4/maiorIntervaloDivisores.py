from math import sqrt

n = int(input())

def divisores(number):
    l = []

    for i in range(1, int(sqrt(number)) + 1):
        if n % i == 0:
            l.append(i)

    max_length = 1
    current_length = 1

    for i in range(1, len(l)):
        if l[i] == l[i - 1] + 1:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length

for i in range(n):
    numero = int(input())
    print(divisores(numero))
