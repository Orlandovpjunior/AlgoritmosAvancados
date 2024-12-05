tamanho = int(input())
entrada = list(map(int, input().split()))

lista = set()
l = 0
h = 0
contador = 1
contador_max = 1

while h < tamanho:
    if entrada[h] not in lista:
        lista.add(entrada[h])
        contador += 1
        h += 1
    else:
        l = h
        contador_max = max(contador, contador_max)
        contador = 1