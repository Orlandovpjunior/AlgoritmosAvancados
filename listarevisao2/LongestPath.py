import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

adj = {i: [] for i in range(1, n + 1)}
visited = [False] * (n + 1)
topo = []

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)

def dfs(u):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            dfs(v)
    topo.append(u)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)

topo.reverse()

dp = [0] * (n + 1)

for u in topo:
    for v in adj[u]:
        dp[v] = max(dp[v], dp[u] + 1)

print(max(dp))
