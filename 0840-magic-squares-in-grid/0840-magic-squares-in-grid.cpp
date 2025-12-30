class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int r = grid.size();
        int c = grid[0].size();
        int count = 0;

        for (int i = 0; i + 2 < r; i++) {
            for (int j = 0; j + 2 < c; j++) {
                if (isMagic(grid, i, j)) {
                    count++;
                }
            }
        }
        return count;
    }

    bool isMagic(vector<vector<int>>& g, int i, int j) {
        if (g[i+1][j+1] != 5) return false;

        bool seen[10] = {false};
        for (int x = i; x < i + 3; x++) {
            for (int y = j; y < j + 3; y++) {
                int v = g[x][y];
                if (v < 1 || v > 9 || seen[v]) return false;
                seen[v] = true;
            }
        }

        return (
            g[i][j] + g[i][j+1] + g[i][j+2] == 15 &&
            g[i+1][j] + g[i+1][j+1] + g[i+1][j+2] == 15 &&
            g[i+2][j] + g[i+2][j+1] + g[i+2][j+2] == 15 &&
            g[i][j] + g[i+1][j] + g[i+2][j] == 15 &&
            g[i][j+1] + g[i+1][j+1] + g[i+2][j+1] == 15 &&
            g[i][j+2] + g[i+1][j+2] + g[i+2][j+2] == 15 &&
            g[i][j] + g[i+1][j+1] + g[i+2][j+2] == 15 &&
            g[i][j+2] + g[i+1][j+1] + g[i+2][j] == 15
        );
    }
};
