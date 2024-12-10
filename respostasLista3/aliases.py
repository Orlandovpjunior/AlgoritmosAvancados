qtdNomes = int(input())
apelidos = dict()

contador = 0
for i in range(qtdNomes):
    dados = input().split()
    num_nomes = int(dados[0])
    nomes = dados[1:]
    aux = ''.join([nome[0] for nome in nomes])
    if aux in apelidos:
        apelidos[aux] += 1
    else:
        apelidos[aux] = 1

contador = 0

for apelido in apelidos:
    if apelidos[apelido] == 1:
        contador += 1
print(contador)