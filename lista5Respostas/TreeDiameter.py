import sys
from collections import deque, defaultdict

def bfs(inicio, grafo):
    fila = deque([(inicio, 0)])
    visitados = set([inicio])
    node_mais_distante, maior_distancia = inicio, 0

    while fila:
        node, dist = fila.popleft()
        if dist > maior_distancia:
            node_mais_distante, maior_distancia = node, dist

        for vizinho in grafo[node]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, dist + 1))

    return node_mais_distante, maior_distancia

def tree_diameter(n, edges):
    if n == 1:
        return 0

    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    farthest_node, _ = bfs(1, graph)

    _, diameter = bfs(farthest_node, graph)

    return diameter

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    input = sys.stdin.read
    data = input().split("\n")
    
    n = int(data[0].strip())
    edges = [tuple(map(int, line.split())) for line in data[1:] if line]

    print(tree_diameter(n, edges))
