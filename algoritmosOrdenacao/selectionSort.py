lista = [10, 2, 1, 5]

for i in range(len(lista)):
    menor = lista[i]
    pos_menor = i
    for j in range(i + 1, len(lista)):
        if lista[j] < menor:
            menor = lista[j]
            pos_menor = j
    
    lista[pos_menor] = lista[i]
    lista[i] = menor

print(lista)