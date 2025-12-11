class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        rows = {}
        cols = {}
        for x, y in buildings:
            if x not in rows:
                rows[x] = []
            rows[x].append(y)
            if y not in cols:
                cols[y] = []
            cols[y].append(x)

        for r in rows:
            rows[r].sort()
        for c in cols:
            cols[c].sort()

        def bisect_left(a, x):
            l, r = 0, len(a)
            while l < r:
                m = (l + r) // 2
                if a[m] < x:
                    l = m + 1
                else:
                    r = m
            return l

        ans = 0
        for x, y in buildings:
            row = rows[x]
            col = cols[y]

            p_row = bisect_left(row, y)
            if p_row == 0 or p_row == len(row) - 1:
                continue

            p_col = bisect_left(col, x)
            if p_col == 0 or p_col == len(col) - 1:
                continue

            ans += 1

        return ans
        