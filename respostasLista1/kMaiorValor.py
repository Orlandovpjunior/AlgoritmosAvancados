tamanho, consultas = map(int, input().split())
matx = list(map(int, input().split()))

contadorDeUm = sum(matx)

for i in range(consultas):
    entrada = input().split()
    k = int(entrada[0]) 
    t = int(entrada[1])

    if k == 1:
        t -= 1
        if matx[t] == 1:
            contadorDeUm -= 1
        if matx[t] == 0:
            contadorDeUm += 1

        matx[t] = 1 - matx[t]
    if k == 2:
        if t <= contadorDeUm:
            print(1)
        else:
            print(0)