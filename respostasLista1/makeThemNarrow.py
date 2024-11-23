def calculaMin(tamanho, qtdeRemover, arr):
    arr.sort()

    menor = float("inf")

    for i in range(qtdeRemover + 1):
        min_diff = arr[i + (tamanho - qtdeRemover - 1)] - arr[i]
        menor = min(menor,min_diff)

    return menor

t, r = map(int, input().split())
seq = list(map(int, input().split()))

print(calculaMin(t,r,seq))