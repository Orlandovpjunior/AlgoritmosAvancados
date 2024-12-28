from queue import PriorityQueue

entrada = int(input())

for i in range(entrada):
    tamanho = int(input())
    numeros = list(map(int, input().split()))
    dicionario = {i: 0 for i in numeros}

    for num in numeros:
        dicionario[num] += 1

    fila = PriorityQueue()

    for key, value in dicionario.items():
        fila.put(-value)

    while fila.qsize() >= 2:
        a = -fila.get()
        b = -fila.get()

        a -= 1
        b -= 1

        if a > 0:
            fila.put(-a)
        if b > 0:
            fila.put(-b)

    if fila.empty():
        print(0)
    else:
        print(-fila.get())
