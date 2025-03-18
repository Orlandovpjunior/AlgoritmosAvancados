def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, u ,v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    if root_u != root_v:

        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_v] > rank[root_u]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1
        return True
    return False

def kruskal(n, edges):
    edges.sort(key= lambda x: x[2])
    parent = list(range(n))
    rank = [0] * n
    contador = 0
    custo = 0

    for u,v,w in edges:
        if union(parent, rank, u, v):
            custo += w
        if contador == n - 1:
            break
    
    return custo


while True:
    n,m = map(int, input().split())

    if n == 0 and m == 0:
        break
    custo_total = 0
    edges = []
    for _ in range(m):
        a,b,c = map(int, input().split())
        edges.append((a,b,c))
        custo_total += c
    
    custo = kruskal(m, edges)

    print(custo_total - custo)