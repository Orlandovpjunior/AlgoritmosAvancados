t = int(input())

for _ in range(t):
    ver, edg = map(int, input().split())
    graus = {}
    count = {}
    grafo = {}
    
    for _ in range(edg):
        u, v = map(int, input().split())
        graus[u] = graus.get(u, 0) + 1
        graus[v] = graus.get(v, 0) + 1
        if u not in grafo:
            grafo[u] = []
        if v not in grafo:
            grafo[v] = []
        grafo[u].append(v)
        grafo[v].append(u)
    
    maxi = 0
    
    for key, value in graus.items():
        if value == 1:
            if key in grafo:
                for neighbor in grafo[key]:
                    count[neighbor] = count.get(neighbor, 0) + 1
                    maxi = max(maxi, count[neighbor])
    
    print(len(count), maxi)
