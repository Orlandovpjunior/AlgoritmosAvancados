from queue import Queue

def calculaVitorias(Arrlutadores):
    dic = {i + 1: [0, 0] for i in range(len(Arrlutadores))}

    lutador = Arrlutadores[0]
    jogador, rodadas = list(map(int, input().split()))

    maior = max(Arrlutadores)
    indice_maior = Arrlutadores.index(maior) + 1
    if jogador > indice_maior:
        return 0
    else:
        contadorRodadas = 1
        while contadorRodadas <= rodadas:
            topo = fila.get()

            if lutador > topo:
                fila.put(topo)
                dic[Arrlutadores.index(lutador) + 1][0] += 1
                dic[Arrlutadores.index(lutador) + 1][1] += 1
            else:
                fila.put(lutador)
                lutador = topo
                dic[Arrlutadores.index(lutador) + 1][0] += 1
                dic[Arrlutadores.index(lutador) + 1][1] += 1

            contadorRodadas += 1

        return dic[jogador][1]


entrada = int(input())
for i in range(entrada):
    tamanho, perguntas = list(map(int, input().split()))
    lutadores = list(map(int, input().split()))
    fila = Queue()
    for l in lutadores[1:]:
        fila.put(l)
    for i in range(perguntas):
        print(calculaVitorias(lutadores))
    