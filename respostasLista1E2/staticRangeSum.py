tamanho, consultas = map(int, input().split())
lista = list(map(int, input().split()))

arrSomas = [0]

for i in range(len(lista)):
    arrSomas.append(arrSomas[-1] + lista[i])

for i in range(consultas):
    a, b = map(int, input().split())
    print(arrSomas[b] - arrSomas[a - 1])
    