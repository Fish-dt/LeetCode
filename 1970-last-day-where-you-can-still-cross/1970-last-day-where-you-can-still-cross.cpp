class Solution {
public:
    int parent[200005], rank[200005];
    int R, C;
    int topNode, bottomNode;

    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }

    void unite(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) return;
        if (rank[x] < rank[y]) swap(x, y);
        parent[y] = x;
        if (rank[x] == rank[y]) rank[x]++;
    }

    int id(int r, int c) {
        return r * C + c;
    }

    int latestDayToCross(int row, int col, vector<vector<int>>& cells) {
        R = row;
        C = col;
        int n = row * col;
        topNode = n;
        bottomNode = n + 1;

        for (int i = 0; i < n + 2; i++) {
            parent[i] = i;
            rank[i] = 0;
        }

        vector<vector<int>> grid(row, vector<int>(col, 1));
        vector<int> dr = {1, -1, 0, 0};
        vector<int> dc = {0, 0, 1, -1};

        for (int day = cells.size() - 1; day >= 0; day--) {
            int r = cells[day][0] - 1;
            int c = cells[day][1] - 1;
            grid[r][c] = 0;

            int cur = id(r, c);

            if (r == 0) unite(cur, topNode);
            if (r == row - 1) unite(cur, bottomNode);

            for (int d = 0; d < 4; d++) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (nr >= 0 && nr < row && nc >= 0 && nc < col && grid[nr][nc] == 0) {
                    unite(cur, id(nr, nc));
                }
            }

            if (find(topNode) == find(bottomNode))
                return day;
        }
        return 0;
    }
};
