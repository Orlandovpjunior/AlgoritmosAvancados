from queue import Queue

repeticoes = int(input())

for i in range(repeticoes):
    qtde, perguntas = list(map(int, input().split()))
    jogadores = list(map(int, input().split()))
    q = Queue()

    for j in range(1, qtde):
        q.put(jogadores[j])
    
    jogador = jogadores[0]
    for j in range(perguntas):
        numJogador, rounds = list(map(int, input().split()))
        dicionario = dict()

        atual = q.get()

        if jogador > atual:
            q.put(atual)
            if jogador not in dicionario:
                dicionario[jogador] = 1
            else:
                dicionario[jogador] += 1
        else:
            q.put(jogador)
            jogador = atual
            if atual not in dicionario:
                dicionario[atual] = 1
            else:
                dicionario[atual] += 1
        print(dicionario)