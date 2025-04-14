def dfs(start, adj, visited):
    stack = [start]
    visited[start] = True

    while stack:
        v = stack.pop()
        for w in adj[v]:
            if not visited[w]:
                stack.append(w)
                visited[w] = True

n,m = map(int, input().split())

adj = {i:[] for i in range(1, n + 1)}
visited = [False] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(b)

componentes = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i,adj,visited)
        componentes += 1

print(componentes)
