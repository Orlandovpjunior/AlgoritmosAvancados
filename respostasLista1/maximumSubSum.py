
tamanho = int(input())
numeros = list(map(int, input().split()))

maior = numeros[0]
sumAcum = 0

l = 0
h = 0

for i in range(tamanho):
        
    sumAcum += numeros[h]
    h += 1
    maior = max(sumAcum, maior)
    if sumAcum < 0:
        l = h
        sumAcum = 0


print(maior)