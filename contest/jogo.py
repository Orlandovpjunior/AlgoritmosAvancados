directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
              (-1, -1), (-1, 1), (1, -1), (1, 1)]

def dfs(x, y, board, memo, h, w):
    if memo[x][y] != -1:
        return memo[x][y]
    
    max_len = 1
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w:
            if ord(board[nx][ny]) == ord(board[x][y]) + 1:
                max_len = max(max_len, 1 + dfs(nx, ny, board, memo, h, w))
    
    memo[x][y] = max_len
    return max_len

case = 1
while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break

    board = [input() for _ in range(h)]
    memo = [[-1] * w for _ in range(h)]
    
    result = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 'A':
                result = max(result, dfs(i, j, board, memo, h, w))
    
    print(f"Case {case}: {result}")
    case += 1
