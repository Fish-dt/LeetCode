class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        r = m - 1
        c = 0
        ans = 0
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                ans += n - c
                r -= 1
            else:
                c += 1
        return ans
        