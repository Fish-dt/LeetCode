class Solution(object):
    def rangeAddQueries(self, n, queries):
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1

        mat = [[0] * n for _ in range(n)]
        
        for r in range(n):
            for c in range(n):
                diff[r][c] += diff[r][c - 1] if c > 0 else 0
        
        for c in range(n):
            for r in range(n):
                diff[r][c] += diff[r - 1][c] if r > 0 else 0
        
        for r in range(n):
            for c in range(n):
                mat[r][c] = diff[r][c]

        return mat
        