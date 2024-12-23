from queue import PriorityQueue

entrada = int(input())

for i in range(entrada):
    qtde = int(input())
    pessoas = list(map(int, input().split()))
    pessoasReuniao = PriorityQueue()

    for index, valor in enumerate(pessoas):
        if valor > 0:
            pessoasReuniao.put((-valor, index + 1))
    
    interacoes = []

    while pessoasReuniao.qsize() > 1:
        pessoa1 = pessoasReuniao.get()
        pessoa2 = pessoasReuniao.get()
        interacoes.append((pessoa1[1], pessoa2[1]))

        nova_pessoa1 = (pessoa1[0] + 1, pessoa1[1])
        nova_pessoa2 = (pessoa2[0] + 1, pessoa2[1])
        
        if nova_pessoa1[0] < 0:
            pessoasReuniao.put(nova_pessoa1)
        if nova_pessoa2[0] < 0:
            pessoasReuniao.put(nova_pessoa2)
    
    print(len(interacoes))

    for interacao in interacoes:
        print(interacao[0], interacao[1])
