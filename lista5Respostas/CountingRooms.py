from collections import deque

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]  

direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y):
    fila = deque([(x, y)])
    grid[x][y] = '#'  # Marca como visitado

    while fila:
        cx, cy = fila.popleft()

        for dx, dy in direcoes:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.':
                grid[nx][ny] = '#'  # Marca como visitado
                fila.append((nx, ny))  # Adiciona à fila para explorar depois

rooms = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':  # Nova sala encontrada
            bfs(i, j)  # Explorar toda a sala com BFS
            rooms += 1  # Conta a nova sala

print(rooms)
