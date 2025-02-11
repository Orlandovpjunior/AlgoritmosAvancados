def G(n):

    contador = 0

    if n == 1:
        return contador
    else:
        while pow(2, contador) <= n:
            contador += 1
    return contador - 1

n = int(input())
print(G(n))

