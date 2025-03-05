import heapq

n, m = map(int, input().split())

grafo = {i: {} for i in range(1, n + 1)}
pais = {i: None for i in range(1, n + 1)}

for _ in range(m):
    ai,bi,wi = map(int, input().split())

    grafo[ai][bi] = wi
    grafo[bi][ai] = wi

infinito = float('inf')

custos = {i: infinito for i in range(1, n + 1)}
custos[1] = 0
fila = [(0,1)]
heapq.heapify(fila)

while fila:

    custo_atual, node_atual = heapq.heappop(fila)

    for node, peso in grafo[node_atual].items():
        novo_custo = custo_atual + peso

        if novo_custo < custos[node]:
            custos[node] = novo_custo
            pais[node] = node_atual
            heapq.heappush(fila, (novo_custo, node))
    
if custos[n] == infinito:
    print(-1)
else:
    caminho = []
    atual = n

    while atual is not None:
        caminho.append(atual)
        atual = pais[atual]
    
    caminho.reverse()
    print(*caminho)


