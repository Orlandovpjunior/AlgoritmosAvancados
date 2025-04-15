from collections import deque

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'A':
            start = (i, j)
        if board[i][j] == 'B':
            end = (i, j)

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
move_char = ['U', 'D', 'L', 'R']

visited = [[False]*m for _ in range(n)]
parent = [[None]*m for _ in range(n)]

queue = deque()
queue.append(start)
visited[start[0]][start[1]] = True

found = False

while queue:
    x, y = queue.popleft()
    if (x, y) == end:
        found = True
        break
    for idx, (dx, dy) in enumerate(moves):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] != '#':
            visited[nx][ny] = True
            parent[nx][ny] = (x, y, move_char[idx])
            queue.append((nx, ny))

if not found:
    print("NO")
else:
    print("YES")
    path = []
    x, y = end
    while (x, y) != start:
        px, py, direction = parent[x][y]
        path.append(direction)
        x, y = px, py
    path.reverse()
    print(len(path))
    print(''.join(path))
