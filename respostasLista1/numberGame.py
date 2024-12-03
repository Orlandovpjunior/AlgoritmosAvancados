def contemNumero(array, numero):
    for i in range(len(array)):
        if array[i] <= numero:
            del array[i]
            return True
    return False

def jogo(numeros):
    k = 1 
    numeros.sort()

    for i in range(1, len(numeros) + 1):
        if contemNumero(numeros, k - i + 1):
            k += 1
        else:
            break
    return k - 1 

numTestes = int(input())
for i in range(numTestes):
    quantidade = int(input())
    numeros = list(map(int, input().split()))
    print(jogo(numeros))
