#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, m;
vector<vector<char>> grid;

// Direções possíveis para movimentação (cima, baixo, esquerda, direita)
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

// BFS para percorrer um cômodo e marcá-lo como visitado
void bfs(int x, int y) {
    queue<pair<int, int>> q;
    q.push({x, y});
    grid[x][y] = '#'; // Marca como visitado

    while (!q.empty()) {
        auto [cx, cy] = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];

            // Verifica se a nova posição está dentro dos limites e é um piso '.'
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && grid[nx][ny] == '.') {
                grid[nx][ny] = '#'; // Marca como visitado
                q.push({nx, ny});
            }
        }
    }
}

int countRooms() {
    int roomCount = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == '.') {
                bfs(i, j);
                roomCount++; // Incrementa o número de cômodos encontrados
            }
        }
    }
    return roomCount;
}

int main() {
    ios::sync_with_stdio(false); // Otimiza entrada e saída
    cin.tie(nullptr);

    cin >> n >> m;
    grid.resize(n, vector<char>(m));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
        }
    }

    cout << countRooms() << "\n";

    return 0;
}
