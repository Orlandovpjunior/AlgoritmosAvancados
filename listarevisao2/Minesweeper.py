h, w = map(int,input().split())
grid = [list(input()) for _ in range(h)]

result = [['' for _ in range(w)] for _ in range(h)] 

directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),(0, 1),
              (1,-1), (1,0), (1,1)]

for i in range(h):
    for j in range(w):
        if grid[i][j] == '#':
            result[i][j] = "#"
        else:
            count = 0
            for dx, dy in directions:
                ni = i + dx
                nj = j + dy

                if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == '#':
                    count += 1
            result[i][j] = str(count)

for linha in result:
    print(''.join(linha))

