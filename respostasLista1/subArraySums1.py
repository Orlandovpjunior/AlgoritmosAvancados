tamanho, alvo = list(map(int, input().split()))
entrada = list(map(int, input().split()))

contador = 0
inicio = 0
soma = 0

for i in range(tamanho):
    soma += entrada[i]

    while soma > alvo and inicio <= i:
        soma -= entrada[inicio]
        inicio += 1

    if soma == alvo:
        contador += 1

print(contador)



