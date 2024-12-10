tamanho = int(input())
entrada = list(map(int, input().split()))

lista = set()
l = 0
h = 0
contador = 1
contador_max = 1

while h < tamanho:
    if entrada[h] in lista:
        lista.remove(entrada[l])
        l += 1
    else:
        lista.add(entrada[h])
        h += 1
        contador_max = max(contador_max, len(lista))

print(contador_max)
