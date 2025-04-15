def dfs(node ,start, depth, graph):
    if depth == 3:
        return node == start
    next_node = graph[node]
    return dfs(next_node, start, depth + 1, graph)

n = int(input())
f = list(map(int, input().split()))
found = False

graph = [x - 1 for x in f]

for i in range(n):
    if dfs(i,i,0,graph):
        found = True
        break

print("YES" if found else "NO")