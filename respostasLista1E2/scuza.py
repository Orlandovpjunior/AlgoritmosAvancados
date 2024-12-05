casos = int(input())

for i in range(casos):
    tamanho, qtdPerguntas = list(map(int, input().split()))
    entrada = list(map(int, input().split()))

    p = [0] * (tamanho + 1)
    v = [0] * (tamanho)
    current = 0
    for j in range(1, tamanho + 1):
        p[j] = p[j - 1] + entrada[j - 1]
        current = max(current, entrada[j - 1])
        v[j - 1] = current

    perguntas = list(map(int, input().split()))
    respostas = []

    for num in perguntas:
        left, right = 0, tamanho
        while left < right:
            middle = (left + right) // 2
            if v[middle] <= num:
                left = middle + 1
            else:
                right = middle
        respostas.append(p[left])

    print(' '.join(map(str, respostas)))
