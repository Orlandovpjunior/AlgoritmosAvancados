t = int(input())

for _ in range(t):
    n = int(input())

    inimigo = list(input())
    greg = list(input())
    contador = 0

    for i in range(n):

        if greg[i] == '1':
            if inimigo[i] == '0':
                contador += 1
                inimigo[i] = 'x'
            elif i > 0 and inimigo[i - 1] == '1':
                contador += 1
                inimigo[i - 1] = 'x'
            elif i < n - 1 and inimigo[i + 1] == '1':
                contador += 1
                inimigo[i + 1] = 'x'
    print(contador)