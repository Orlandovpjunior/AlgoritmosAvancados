casos = int(input())

for i in range(casos):
    entrada = input()
    pilha = []

    for c in entrada:
        if pilha and c == 'B':
            pilha.pop()
        else:
            pilha.append(c)
    print(len(pilha))


