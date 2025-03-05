#Solução dando TLE
import heapq

n,m  = map(int, input().split())

grafo = {i: [] for i in range(1, n+1)}
infinito = float("inf")


for _ in range(m):
    a,b,c = map(int, input().split())
    grafo[a].append((b,c))

custos = {i: [infinito,infinito] for i in range(1, n+1)}
custos[1][0] = 0
fila = [(0,1,0)]
heapq.heapify(fila)

while fila:
    custo_atual, nodo_atual, cupom = heapq.heappop(fila)

    if custo_atual > custos[nodo_atual][cupom]:
        continue

    for node, peso in grafo[nodo_atual]:
        novo_custo = custo_atual + peso

        if novo_custo < custos[node][cupom]:
            custos[node][cupom] = novo_custo
            heapq.heappush(fila, (novo_custo, node, cupom))

        if cupom == 0:
            novo_custo_cupom = custo_atual + (peso // 2)
            if novo_custo_cupom < custos[node][1]:
                custos[node][1] = novo_custo_cupom
                heapq.heappush(fila, (novo_custo_cupom, node, 1))

print(custos[n][1])
